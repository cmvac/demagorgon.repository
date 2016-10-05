# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/MetallicaTv
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.metallicatv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID1 = "metallicatv"
YOUTUBE_CHANNEL_ID2 = "fullconcerts100"
YOUTUBE_CHANNEL_ID3 = "ccastr0"
# Entry point
def run():
    plugintools.log("metallicatv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("metallicatv.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Enter Metallica TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Metallica Full Concerts",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID2+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Metallica Full Albums",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID3+"/",
        thumbnail=icon,
        folder=True )

run()