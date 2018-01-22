import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "/storage/hyperion/bin/hyperiond.sh /storage/.config/hyperion.config.json </dev/null >/dev/null 2>&1 &"
os.system(cmd) 
xbmcgui.Dialog().ok(addonname, "Ambilight is now turned on.")