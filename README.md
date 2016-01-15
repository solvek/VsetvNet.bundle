# Overview

Allows to watch content from site [VseTV.Net](vsetv.net).
Currently videos are not playing, the problem is logged [here](https://forums.plex.tv/discussion/202747/playing-videos-from-site-vsetv-net#latest).

# Installation

Follow [manual installation instructions ](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-)from here.

# Useful development information

* [Web Admin for plex](http://localhost:32400/web/index.html)
* Starting plex server: `sudo /etc/init.d/plexmediaserver start`
* Restarting plex server: `sudo service plexmediaserver restart`
* Log file: `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.vsetvnet.log`
* [Test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fvsetv.net%2Fpiksel.html)
* [TuneIn test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fopml.radiotime.com%2FTune.ashx)
