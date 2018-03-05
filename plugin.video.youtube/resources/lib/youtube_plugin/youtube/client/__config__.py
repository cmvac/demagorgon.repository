# -*- coding: utf-8 -*-

from base64 import b64decode
from hashlib import md5
from ...kodion.json_store import APIKeyStore
from ...kodion import Context as __Context
from ... import key_sets

DEFAULT_SWITCH = 1

__context = __Context(plugin_id='plugin.video.youtube')
__settings = __context.get_settings()


class APICheck(object):

    def __init__(self, context):
        self._context = context
        self._settings = context.get_settings()
        self._ui = context.get_ui()
        self._api_jstore = APIKeyStore()
        self._json_api = self._api_jstore.get_data()

        self.changed = False

        self._on_init()

    def _on_init(self):
        self._json_api = self._api_jstore.get_data()

        j_key = self._json_api['keys']['personal'].get('api_key', '')
        j_id = self._json_api['keys']['personal'].get('client_id', '')
        j_secret = self._json_api['keys']['personal'].get('client_secret', '')

        original_key = self._settings.get_string('youtube.api.key')
        original_id = self._settings.get_string('youtube.api.id')
        original_secret = self._settings.get_string('youtube.api.secret')

        own_key, own_id, own_secret = self._strip_api_keys(original_key, original_id, original_secret)

        do_key_load = None
        if (j_key and j_id and j_secret) and (not own_id or not own_key or not own_secret):
            do_key_load = self._ui.on_yes_no_input(title=self._context._plugin_name, text=self._context.localize(30639))
            if do_key_load:
                own_key = j_key
                own_id = j_id
                own_secret = j_secret

                self._json_api['keys']['personal'] = {'api_key': own_key, 'client_id': own_id, 'client_secret': own_secret}

                self._settings.set_string('youtube.api.key', own_key)
                self._settings.set_string('youtube.api.id', own_id)
                self._settings.set_string('youtube.api.secret', own_secret)
                self._settings.set_bool('youtube.api.enable', True)
                self._settings.set_string('youtube.api.last.hash', self._get_key_set_hash('own'))

                self._api_jstore.save(self._json_api)

        if (j_key != own_key) or (j_id != own_id) or (j_secret != own_secret):
            self._json_api['keys']['personal'] = {'api_key': own_key, 'client_id': own_id, 'client_secret': own_secret}
            self._api_jstore.save(self._json_api)

        original = (original_key == own_key) and (original_id == own_id) and (original_secret == own_secret)
        if not original and not do_key_load:
            self._settings.set_string('youtube.api.key', own_key)
            self._settings.set_string('youtube.api.id', own_id)
            self._settings.set_string('youtube.api.secret', own_secret)
        switch = self.get_current_switch()
        updated_hash = self._api_keys_changed(switch)
        if updated_hash:
            self._context.log_warning('Switching API key set to %s' % switch)
            self._settings.set_string('youtube.api.last.hash', updated_hash)
            self._context.log_debug('API key set changed: Signing out')
            self._context.execute('RunPlugin(plugin://plugin.video.youtube/sign/out/?confirmed=true)')
        else:
            self._context.log_debug('Using API key set: %s' % switch)

    def get_current_switch(self):
        return 'own' if self.has_own_api_keys() else self._settings.get_string('youtube.api.key.switch', str(DEFAULT_SWITCH))

    def has_own_api_keys(self):
        own_key = self._settings.get_string('youtube.api.key')
        own_id = self._settings.get_string('youtube.api.id')
        own_secret = self._settings.get_string('youtube.api.secret')
        return False if not own_key or \
                        not own_id or \
                        not own_secret or \
                        not self._settings.get_string('youtube.api.enable') == 'true' else True

    def get_api_keys(self, switch):
        if not switch or (switch == 'own' and not self.has_own_api_keys()):
            switch = '1'
        if switch == 'youtube-tv':
            api_key = b64decode(key_sets['youtube-tv']['key']).decode('utf-8'),
            client_id = b64decode(key_sets['youtube-tv']['id']).decode('utf-8') + u'.apps.googleusercontent.com'
            client_secret = b64decode(key_sets['youtube-tv']['secret']).decode('utf-8')
        elif switch == 'developer':
            self._json_api = self._api_jstore.get_data()
            return self._json_api['keys']['developer']
        elif switch == 'own':
            api_key = self._settings.get_string('youtube.api.key')
            client_id = self._settings.get_string('youtube.api.id') + u'.apps.googleusercontent.com'
            client_secret = self._settings.get_string('youtube.api.secret')
        else:
            api_key = b64decode(key_sets['provided'][switch]['key']).decode('utf-8')
            client_id = b64decode(key_sets['provided'][switch]['id']).decode('utf-8') + u'.apps.googleusercontent.com'
            client_secret = b64decode(key_sets['provided'][switch]['secret']).decode('utf-8')
        return api_key, client_id, client_secret

    def _api_keys_changed(self, switch):
        if not switch or (switch == 'own' and not self.has_own_api_keys()):
            switch = '1'
        last_set_hash = self._settings.get_string('youtube.api.last.hash')
        current_set_hash = self._get_key_set_hash(switch)
        if last_set_hash != current_set_hash:
            self.changed = True
            return current_set_hash
        else:
            self.changed = False
            return None

    def _get_key_set_hash(self, switch):
        if not switch or (switch == 'own' and not self.has_own_api_keys()):
            switch = '1'
        api_key, client_id, client_secret = self.get_api_keys(switch)
        if switch == 'own':
            client_id = client_id.replace(u'.apps.googleusercontent.com', u'')
        m = md5()
        m.update(api_key.encode('utf-8'))
        m.update(client_id.encode('utf-8'))
        m.update(client_secret.encode('utf-8'))

        return m.hexdigest()

    def _strip_api_keys(self, api_key, client_id, client_secret):

        stripped_key = ''.join(api_key.split())
        stripped_id = ''.join(client_id.replace('.apps.googleusercontent.com', '').split())
        stripped_secret = ''.join(client_secret.split())

        if api_key != stripped_key:
            if stripped_key not in api_key:
                self._context.log_debug('Personal API setting: |Key| Skipped: potentially mangled by stripping')
                return_key = api_key
            else:
                self._context.log_debug('Personal API setting: |Key| had whitespace removed')
                return_key = stripped_key
        else:
            return_key = api_key

        if client_id != stripped_id:
            if stripped_id not in client_id:
                self._context.log_debug('Personal API setting: |Id| Skipped: potentially mangled by stripping')
                return_id = client_id
            else:
                googleusercontent = ''
                if '.apps.googleusercontent.com' in client_id:
                    googleusercontent = ' and .apps.googleusercontent.com'
                self._context.log_debug('Personal API setting: |Id| had whitespace%s removed' % googleusercontent)
                return_id = stripped_id
        else:
            return_id = client_id

        if client_secret != stripped_secret:
            if stripped_secret not in client_secret:
                self._context.log_debug('Personal API setting: |Secret| Skipped: potentially mangled by stripping')
                return_secret = client_secret
            else:
                self._context.log_debug('Personal API setting: |Secret| had whitespace removed')
                return_secret = stripped_secret
        else:
            return_secret = client_secret

        return return_key, return_id, return_secret


_api_check = APICheck(__context)

api = dict()
youtube_tv = dict()
keys_changed = _api_check.changed
current_switch = _api_check.get_current_switch()

api['key'], api['id'], api['secret'] = _api_check.get_api_keys(current_switch)

youtube_tv['key'], youtube_tv['id'], youtube_tv['secret'] = _api_check.get_api_keys('youtube-tv')

developer_keys = _api_check.get_api_keys('developer')
