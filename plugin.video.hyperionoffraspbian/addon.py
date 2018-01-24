import xbmcaddon
import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

     # kill hyperiond and rename config files
cmd = "sudo systemctl stop hyperion.service 2>/dev/null; sudo /etc/init.d/hyperion stop 2>/dev/null ; sudo /sbin/initctl stop hyperion 2>/dev/null"
os.system(cmd) 