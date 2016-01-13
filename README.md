# Overview

Allows to watch content from site [VseTV.Net](vsetv.net).

# Installation

1. Must have [Plex Media Server][GetPlex] installed, obviously;
2. Download the [zip archive](https://github.com/solvek/VsetvNet.bundle/archive/master.zip) and extract it to Plex plugin folder, for more details read the [official channel installation guide](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-):
  * on Windows: *C:\Users\USERNAME\AppData\Local\Plex Media Server\Plug-ins*
  * on Mac: *~Library/Application Support/Plex Media Server/Plug-ins*
  * on Linux: */usr/lib/plexmediaserver/Resources/Plug-ins* or */var/lib/plex/Plex Media Server/Plug-ins*
  * on FreeBSD *usr/pbi/plexmediaserver-amd64/plexdata/Plex\ Media\ Server/Plug-ins/*
3. Rename folder from *VsetvNet.bundle-master* to *VsetvNet.bundle*;
4. Restart the Plex Media Server;
5. Launch any of [Plex Apps][GetPlex] (that is connected to the server, obviously) and you should see a new category in Your media library called Video Channels or similar.

# Useful development information

* [Web Admin for plex](http://localhost:32400/web/index.html)
* Starting plex server: `sudo /etc/init.d/plexmediaserver start`
* Restarting plex server: `sudo service plexmediaserver restart`
* Log file: `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs/com.plexapp.plugins.vsetvnet.log`
* [Test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fvsetv.net%2Fpiksel.html)
* [TuneIn test service](http://localhost:32400/system/services/url/lookup?url=http%3A%2F%2Fopml.radiotime.com%2FTune.ashx)
