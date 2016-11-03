import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "killall hyperiond"
os.system(cmd) 
xbmcgui.Dialog().ok(addonname, "Ambilight is now turned off.")