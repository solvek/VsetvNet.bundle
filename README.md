# Overview

Allows to watch content from site [VseTV.Net](vsetv.net).

# Installation

Follow [manual installation instructions ](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-)from here.

# Tested players

 * Samsung Smart TV
 * Android Plex TV app

# Useful development information

* [Web Admin for plex](http://localhost:32400/web/index.html)
* Starting plex server: `sudo /etc/init.d/plexmediaserver start`
* Restarting plex server: `sudo service plexmediaserver restart`
* Log file: `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.vsetvnet.log`
* [Test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fvsetv.net%2Fpiksel.html)
* [TuneIn test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fopml.radiotime.com%2FTune.ashx)
