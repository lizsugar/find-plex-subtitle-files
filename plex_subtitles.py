#!/bin/python3

from plexapi.myplex import MyPlexAccount
import plex_creds

account = MyPlexAccount(plex_creds.plex_account_name, plex_creds.plex_account_password)
plex = account.resource(plex_creds.plex_account_server).connect()

#tvshows = plex.library.section('TV Shows')
show = plex.library.section('TV Shows').get('Batwoman').episodes()[-1]

#print(batwoman)

for ep in show:
  ep.reload()

  #  print(ep.title + " - " + part.file + "\n")

  print(ep.grandparentTitle+ " - " + ep.seasonEpisode + " - " + ep.title)

  for media in ep.media:
    for mpart in media.parts:
      print("\tVIDEO FILE: " + mpart.file)

  print("SUBTITLE STREAMS: ")
  print(ep.subtitleStreams())
  
  print("---\n")

