# -*- coding: utf-8 -*-
#------------------------------------------------------------
# behindmovies
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.behindmovies'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.behindmovies/resources/fan01.png'
icon = 'special://home/addons/plugin.video.behindmovies/resources/icon.png'
icon00 = 'special://home/addons/plugin.video.behindmovies/resources/icon00.png'
icon01 = 'special://home/addons/plugin.video.behindmovies/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.behindmovies/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.behindmovies/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.behindmovies/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.behindmovies/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.behindmovies/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.behindmovies/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.behindmovies/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.behindmovies/resources/icon09.png'
icon10 = 'special://home/addons/plugin.video.behindmovies/resources/icon10.png'
icon11 = 'special://home/addons/plugin.video.behindmovies/resources/icon11.png'
icon12 = 'special://home/addons/plugin.video.behindmovies/resources/icon12.png'
icon13 = 'special://home/addons/plugin.video.behindmovies/resources/icon13.png'
icon14 = 'special://home/addons/plugin.video.behindmovies/resources/icon14.png'
icon15 = 'special://home/addons/plugin.video.behindmovies/resources/icon15.png'
icon16 = 'special://home/addons/plugin.video.behindmovies/resources/icon16.png'
icon17 = 'special://home/addons/plugin.video.behindmovies/resources/icon17.png'
icon18 = 'special://home/addons/plugin.video.behindmovies/resources/icon18.png'
icon19 = 'special://home/addons/plugin.video.behindmovies/resources/icon19.png'
icon20 = 'special://home/addons/plugin.video.behindmovies/resources/icon20.png'
icon21 = 'special://home/addons/plugin.video.behindmovies/resources/icon21.png'
icon22 = 'special://home/addons/plugin.video.behindmovies/resources/icon22.png'
icon23 = 'special://home/addons/plugin.video.behindmovies/resources/icon23.png'
icon24 = 'special://home/addons/plugin.video.behindmovies/resources/icon24.png'
icon25 = 'special://home/addons/plugin.video.behindmovies/resources/icon25.png'
icon26 = 'special://home/addons/plugin.video.behindmovies/resources/icon26.png'
icon27 = 'special://home/addons/plugin.video.behindmovies/resources/icon27.png'
icon28 = 'special://home/addons/plugin.video.behindmovies/resources/icon28.png'



def run():
    plugintools.log("behindmovies.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("behindmovies ===> " + repr(params))
	
	plugintools.add_item(title = "CRACKED", url = base + "playlist/UUjD2KyAEm84yVH8cTilID7Q/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "WATCHMOJO", url = base + "playlist/UUaWd5_7JhbQBe4dknZhsHJg/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "LOOPER", url = base + "playlist/UUP1iRaFlS5EYjJBryFV9JPw/", thumbnail = icon27, fanart = fan01, folder = True)
	plugintools.add_item(title = "FILM IS NOW - BLOOPERS AND EXTRAS", url = base + "playlist/UUmQynT5NWU3Vsa9t0OGUhcA/", thumbnail = icon26, fanart = fan01, folder = True)
	plugintools.add_item(title = "FILM IS NOW - BEST OF MOVIES", url = base + "playlist/UUmXMUE-aowQu94qrulWc6aA/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "THE HOLLYWOOD REPORTER", url = base + "playlist/UUZ8Sxmkweh65HetaZfR8YuA/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "HOLLYWOOD LIFE", url = base + "playlist/UU2rJLq19N0dGrxfib80M_fg/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "EVERY FRAME A PAINTING", url =  base + "playlist/UUjFqcJQXGZ6T6sxyFB-5i6A/", thumbnail = icon06, fanart = fan01, folder = True)
	plugintools.add_item(title = "LESSONS FROM THE SCREENPLAY", url = base + "playlist/UUErSSa3CaP_GJxmFpdjG9Jw/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "NOW YOU SEE IT", url = base + "playlist/UUWTFGPpNQ0Ms6afXhaWDiRw/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "FILM RADAR", url = base + "playlist/UUMplSrEvn9JTCHrz58Le2ww/", thumbnail = icon09, fanart = fan01, folder = True)
	plugintools.add_item(title = "MOVIE BOB", url = base + "playlist/UUy92fXa6yBrLnKdW1pYJlMw/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "RED LETTER MEDIA", url = base + "playlist/UUrTNhL_yO3tPTdQ5XgmmWjA/", thumbnail = icon11, fanart = fan01, folder = True)	
	plugintools.add_item(title = "HOW IT SHOULD HAVE ENDED", url = base + "playlist/UUHCph-_jLba_9atyCZJPLQQ/", thumbnail = icon28, fanart = fan01, folder = True)
	plugintools.add_item(title = "CINEMA SINS", url = base + "playlist/UUYUQQgogVeQY8cMQamhHJcg/", thumbnail = icon12, fanart = fan01, folder = True)
	plugintools.add_item(title = "CHRIS STUCKMANN MOVIE REVIEWS", url = base + "playlist/UUCqEeDAUf4Mg0GgEN658tkA/", thumbnail = icon13, fanart = fan01, folder = True)
	plugintools.add_item(title = "CINEFIX", url = base + "playlist/UUVtL1edhT8qqY-j2JIndMzg/", thumbnail = icon14, fanart = fan01, folder = True)
	plugintools.add_item(title = "MAKING OF", url = base + "playlist/UU99ICt5CBNn7VssX5zp0BnQ/", thumbnail = icon15, fanart = fan01, folder = True)
	plugintools.add_item(title = "GRUNGE", url = base + "playlist/UUWlIGsKGsvgFJHkiZml4O1A/", thumbnail = icon16, fanart = fan01, folder = True)
	plugintools.add_item(title = "SCREENRANT", url = base + "playlist/UU2iUwfYi_1FCGGqhOUNx-iA/", thumbnail = icon18, fanart = fan01, folder = True)
	plugintools.add_item(title = "WHATCULTURE", url = base + "playlist/UUM7Srv4mxJejt2NLmumkRRQ/", thumbnail = icon19, fanart = fan01, folder = True)
	plugintools.add_item(title = "THE FILM THEORISTS", url = base + "playlist/UU3sznuotAs2ohg_U__Jzj_Q/", thumbnail = icon20, fanart = fan01, folder = True)
	plugintools.add_item(title = "SCREEN JUNKIES", url = base + "playlist/UUOpcACMWblDls9Z6GERVi1A/", thumbnail = icon21, fanart = fan01, folder = True)
	plugintools.add_item(title = "AWE ME", url = base + "playlist/UUNKcMBYP_-18FLgk4BYGtfw/", thumbnail = icon22, fanart = fan01, folder = True)
	plugintools.add_item(title = "THE WARP ZONE", url = base + "playlist/UUSOkex4abVl14cZ4tLyUYzw/", thumbnail = icon23, fanart = fan01, folder = True)
	plugintools.add_item(title = "COUCH TOMATO", url = base + "playlist/UUOZcxtwy_YYe7KKky8DCLGQ/", thumbnail = icon24, fanart = fan01, folder = True)
	plugintools.add_item(title = "COLLIDER VIDEOS", url = base + "playlist/UUWvMmm_sSdgALpo1Ci4WvtQ/", thumbnail = icon25, fanart = fan01, folder = True)
		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
