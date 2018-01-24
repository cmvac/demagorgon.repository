import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "killall hyperiond"
os.system(cmd) 
os.rename("/storage/.config/hyperion.config.json", "/storage/.config/hyperion.config2.json")
os.rename("/storage/.config/hyperion.config1.json", "/storage/.config/hyperion.config.json")
os.rename("/storage/.config/hyperion.config2.json", "/storage/.config/hyperion.config1.json")
cmd = "/storage/hyperion/bin/hyperiond.sh /storage/.config/hyperion.config.json </dev/null >/dev/null 2>&1 &"
os.system(cmd)