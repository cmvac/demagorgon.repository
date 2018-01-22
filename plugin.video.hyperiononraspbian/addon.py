import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "sudo systemctl start hyperion.service 2>/dev/null ; sudo /etc/init.d/hyperion start 2>/dev/null ; sudo /sbin/initctl start hyperion 2>/dev/null"
os.system(cmd) 
xbmcgui.Dialog().ok(addonname, "Ambilight is now turned on.")