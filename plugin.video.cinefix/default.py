# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Cinefix
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import xbmc, xbmcaddon, xbmcplugin, os, sys, plugintools
from addon.common.addon import Addon

addonID = 'plugin.video.cinefix'
addon   = Addon(addonID, sys.argv)
local   = xbmcaddon.Addon(id=addonID)
icon    = local.getAddonInfo('icon')
base    = 'plugin://plugin.video.youtube/'

fan01 = 'special://home/addons/plugin.video.cinefix/resources/fan01.png'
icon = 'special://home/addons/plugin.video.cinefix/resources/icon.png'
icon00 = 'special://home/addons/plugin.video.cinefix/resources/icon00.png'
icon01 = 'special://home/addons/plugin.video.cinefix/resources/icon01.png'
icon02 = 'special://home/addons/plugin.video.cinefix/resources/icon02.png'
icon03 = 'special://home/addons/plugin.video.cinefix/resources/icon03.png'
icon04 = 'special://home/addons/plugin.video.cinefix/resources/icon04.png'
icon05 = 'special://home/addons/plugin.video.cinefix/resources/icon05.png'
icon06 = 'special://home/addons/plugin.video.cinefix/resources/icon06.png'
icon07 = 'special://home/addons/plugin.video.cinefix/resources/icon07.png'
icon08 = 'special://home/addons/plugin.video.cinefix/resources/icon08.png'
icon09 = 'special://home/addons/plugin.video.cinefix/resources/icon09.png'
icon10 = 'special://home/addons/plugin.video.cinefix/resources/icon10.png'
icon11 = 'special://home/addons/plugin.video.cinefix/resources/icon11.png'
icon12 = 'special://home/addons/plugin.video.cinefix/resources/icon12.png'
icon13 = 'special://home/addons/plugin.video.cinefix/resources/icon13.png'
icon14 = 'special://home/addons/plugin.video.cinefix/resources/icon14.png'
icon15 = 'special://home/addons/plugin.video.cinefix/resources/icon15.png'
icon16 = 'special://home/addons/plugin.video.cinefix/resources/icon16.png'
icon17 = 'special://home/addons/plugin.video.cinefix/resources/icon17.png'
icon18 = 'special://home/addons/plugin.video.cinefix/resources/icon18.png'
icon19 = 'special://home/addons/plugin.video.cinefix/resources/icon19.png'
icon20 = 'special://home/addons/plugin.video.cinefix/resources/icon20.png'
icon21 = 'special://home/addons/plugin.video.cinefix/resources/icon21.png'
icon22 = 'special://home/addons/plugin.video.cinefix/resources/icon22.png'
icon23 = 'special://home/addons/plugin.video.cinefix/resources/icon23.png'
icon24 = 'special://home/addons/plugin.video.cinefix/resources/icon24.png'
icon25 = 'special://home/addons/plugin.video.cinefix/resources/icon25.png'
icon26 = 'special://home/addons/plugin.video.cinefix/resources/icon26.png'
icon27 = 'special://home/addons/plugin.video.cinefix/resources/icon27.png'
icon28 = 'special://home/addons/plugin.video.cinefix/resources/icon28.png'
icon29 = 'special://home/addons/plugin.video.cinefix/resources/icon29.png'
icon30 = 'special://home/addons/plugin.video.cinefix/resources/icon30.png'
icon31 = 'special://home/addons/plugin.video.cinefix/resources/icon31.png'
icon32 = 'special://home/addons/plugin.video.cinefix/resources/icon32.png'



def run():
    plugintools.log("cinefix.run")
    params = plugintools.get_params()
    if params.get("action") is None: main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def main_list(params):
	plugintools.log("cinefix ===> " + repr(params))
	
	plugintools.add_item(title = "THINGS YOU DID NOT KNOW", url =  base + "playlist/PL1AXWu-gGX6L3AXjKHlxHSXoOsFrBhc8Q/", thumbnail = icon01, fanart = fan01, folder = True)
	plugintools.add_item(title = "8-BIT CINEMA", url = base + "playlist/PL1AXWu-gGX6LNsfQ-KkeGPxL76CFONTom/", thumbnail = icon02, fanart = fan01, folder = True)
	plugintools.add_item(title = "CineFix Roundtable", url = base + "playlist/PL1AXWu-gGX6KRySUOt9sRxaznMFDmt0oi/", thumbnail = icon03, fanart = fan01, folder = True)
	plugintools.add_item(title = "Movie Lists", url = base + "playlist/PL1AXWu-gGX6IcOGt0yaA9Cd_hkt_TwQlC/", thumbnail = icon04, fanart = fan01, folder = True)
	plugintools.add_item(title = "DIY Costume Squad!", url = base + "playlist/PL1AXWu-gGX6J6320gvgPoL6OzoUpqugUS/", thumbnail = icon05, fanart = fan01, folder = True)
	plugintools.add_item(title = "CineFix Reviews", url = base + "playlist/PL1AXWu-gGX6J_jGGFHPwovzTPuKO1iYe-/", thumbnail = icon06, fanart = fan01, folder = True)	
	plugintools.add_item(title = "What's the Difference?", url = base + "playlist/PL1AXWu-gGX6Jmq1jfa0FP2G0gTV4wgptm/", thumbnail = icon07, fanart = fan01, folder = True)
	plugintools.add_item(title = "CineFix Now", url = base + "playlist/PL1AXWu-gGX6JMGCgF1gtbVGlAlTsgYbNV/", thumbnail = icon08, fanart = fan01, folder = True)
	plugintools.add_item(title = "What to Watch Before You Die", url = base + "playlist/PL1AXWu-gGX6I9hsSmaDK1UNEbjcPUhwzG/", thumbnail = icon09, fanart = fan01, folder = True)
	plugintools.add_item(title = "Like It / Love It", url = base + "playlist/PL1AXWu-gGX6L2u0LGl4Eq51tTGEr8ycOY/", thumbnail = icon10, fanart = fan01, folder = True)
	plugintools.add_item(title = "Second Chances", url = base + "playlist/PL1AXWu-gGX6I_lFcOfA939TtuXTm6dHvK/", thumbnail = icon11, fanart = fan01, folder = True)
	plugintools.add_item(title = "Movie Wars", url = base + "playlist/PL1AXWu-gGX6LScbWwiNRweSnG-va8W_BO/", thumbnail = icon12, fanart = fan01, folder = True)
	plugintools.add_item(title = "Art of The Scene", url = base + "playlist/PL1AXWu-gGX6LwUGY1OJ86Jv4fUk1BZy9p/", thumbnail = icon13, fanart = fan01, folder = True)
	plugintools.add_item(title = "Film School'd", url = base + "playlist/PL1AXWu-gGX6LgA7hx3oJEY9vGfrIVOejO/", thumbnail = icon14, fanart = fan01, folder = True)
	plugintools.add_item(title = "Superhero In Training", url = base + "playlist/PL1AXWu-gGX6JnSz8DcAWlWKZUdvWCbAZh/", thumbnail = icon15, fanart = fan01, folder = True)
	plugintools.add_item(title = "Marry, F#@k, Kill", url = base + "playlist/PL1AXWu-gGX6LAhofHWPKr2gAWpP7HKul7/", thumbnail = icon16, fanart = fan01, folder = True)
	plugintools.add_item(title = "Never Before Scene!", url = base + "playlist/PL1AXWu-gGX6KNaqjAwMlnmGM25_zgaNRi/", thumbnail = icon17, fanart = fan01, folder = True)
	plugintools.add_item(title = "Monster Madness Debates!", url = base + "playlist/PL1AXWu-gGX6KV6G4-OuY50Zgb54a5_-5s/", thumbnail = icon18, fanart = fan01, folder = True)
	plugintools.add_item(title = "CineFix Now!", url = base + "playlist/PL1AXWu-gGX6IqkWGx47dzIasYH7aER3h3/", thumbnail = icon19, fanart = fan01, folder = True)
	plugintools.add_item(title = "Master Debaters", url = base + "playlist/PL1AXWu-gGX6JepW8cptNvkHJz74xBIcp3/", thumbnail = icon20, fanart = fan01, folder = True)
	plugintools.add_item(title = "Movies With Kate", url = base + "playlist/PL1AXWu-gGX6LVhvwO3KRfa5Y2uwjXrpdq/", thumbnail = icon21, fanart = fan01, folder = True)
	plugintools.add_item(title = "Bit Rate", url = base + "playlist/PL1AXWu-gGX6JyoT4aw8tFb2F8UXMKk86o/", thumbnail = icon22, fanart = fan01, folder = True)
	plugintools.add_item(title = "60 Second Movie Reviews", url = base + "playlist/PL1AXWu-gGX6JQZsDGWnJQtIwoFOi82csW/", thumbnail = icon23, fanart = fan01, folder = True)
	plugintools.add_item(title = "Interviews", url = base + "playlist/PL1AXWu-gGX6KSaLSJYKq1c-Ed317NkAq2/", thumbnail = icon24, fanart = fan01, folder = True)
	plugintools.add_item(title = "Colleen Ballinger Takes Over Screen Addict", url = base + "playlist/PL1AXWu-gGX6KghgR7MVGdmx37WDSHRcoN/", thumbnail = icon25, fanart = fan01, folder = True)
	plugintools.add_item(title = "The Best Movie Lists", url = base + "playlist/PL1AXWu-gGX6KqeL2EMlRSqPTyWIfnyInV/", thumbnail = icon26, fanart = fan01, folder = True)
	plugintools.add_item(title = "Screen Addict", url = base + "playlist/PL1AXWu-gGX6J5ZAgRZCJKhgq5OowPvdcf/", thumbnail = icon27, fanart = fan01, folder = True)
	plugintools.add_item(title = "Wrong Director", url = base + "playlist/PL1AXWu-gGX6JvgxBavc1qmOM8aSplqxMR/", thumbnail = icon28, fanart = fan01, folder = True)
	plugintools.add_item(title = "8-Bit Game Review", url = base + "playlist/PL1AXWu-gGX6I3fT_syngTf_dj_St3Tl6H/", thumbnail = icon29, fanart = fan01, folder = True)
	plugintools.add_item(title = "Badass Digest", url = base + "playlist/PL1AXWu-gGX6JFH5HwLNKOfOjdKRlsXU2W/", thumbnail = icon30, fanart = fan01, folder = True)
	plugintools.add_item(title = "Conspiracy Cinema", url = base + "playlist/PL1AXWu-gGX6IKCxYN5JrRgf-bCTzg3_3u/", thumbnail = icon31, fanart = fan01, folder = True)
	
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
run()
