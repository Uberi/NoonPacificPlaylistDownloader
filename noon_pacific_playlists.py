#!/usr/bin/env python3

import sys

import requests

playlists = requests.get("https://api.colormyx.com/v1/noon-pacific/playlists/").json()
for entry in playlists:
    print("DOWNLOADING ", entry["name"], file=sys.stderr)
    playlist = requests.get("https://api.colormyx.com/v1/noon-pacific/playlists/{}/tracks/?detail=true".format(entry["id"])).json()
    for song in playlist:
        print("{title}\t{artist}\t{permalink}".format(
            title=song["title"],
            artist=song["artist_description"],
            permalink=song["soundcloud_permalink_url"]
        ))
