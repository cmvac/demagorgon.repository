import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "sudo systemctl stop hyperion.service 2>/dev/null; sudo /etc/init.d/hyperion stop 2>/dev/null ; sudo /sbin/initctl stop hyperion 2>/dev/null"
os.system(cmd) 
os.rename("/storage/.config/hyperion.config.json", "/storage/.config/hyperion.config2.json")
os.rename("/storage/.config/hyperion.config1.json", "/storage/.config/hyperion.config.json")
os.rename("/storage/.config/hyperion.config2.json", "/storage/.config/hyperion.config1.json")
cmd = "sudo systemctl start hyperion.service 2>/dev/null ; sudo /etc/init.d/hyperion start 2>/dev/null ; sudo /sbin/initctl start hyperion 2>/dev/null"
os.system(cmd)
xbmcgui.Dialog().ok(addonname, "Config files swapped. You an swap between internal and external sources now")