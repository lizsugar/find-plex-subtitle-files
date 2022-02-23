#!/bin/python3

from plexapi.myplex import MyPlexAccount
from plexapi.utils import download
import plex_config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("show")
args = parser.parse_args()

# Set up our plex account and connection
account = MyPlexAccount(plex_config.plex_account_name, plex_config.plex_account_password)
plex = account.resource(plex_config.plex_server_name).connect()

# Find Show's Episodes
show = plex.library.section('TV Shows').get(args.show).episodes()[-1]

for ep in show:
  # Gotta reload metadata before subtitle streams will appear for some reason
  ep.reload()


  # Determine container and extension of video file
  epContainer = ""
  for media in ep.media:
    for mpart in media.parts:
      epContainer = mpart.container


  # Generate Downloaded Filenames
  FileName = ep.grandparentTitle+ " - " + ep.seasonEpisode + " - " + ep.title
  videoFileName = FileName + "." + epContainer
  subtitleFileName = FileName + ".srt"

  # Find our subtitle stream with path
  subtitleKey = ""
  for subStream in ep.subtitleStreams():
    if (subStream.key != None):
      subtitleKey = subStream.key


  # Create our downloadable URLs
  videoURL = plex.url(mpart.key, includeToken=True)
  subtitleURL = plex.url(subtitleKey, includeToken=True)


  # Download!
  print("Downloading subtitle file to " + plex_config.subtitleDownloadPath + subtitleFileName)
  download(subtitleURL, plex_config.plex_server_token, filename=subtitleFileName, savepath=plex_config.subtitleDownloadPath, showstatus=True)

  print("Downloading video file to " + plex_config.videoDownloadPath + videoFileName)
  download(videoURL, plex_config.plex_server_token, filename=videoFileName, savepath=plex_config.videoDownloadPath, showstatus=True)
  
  print("---\n")

print("Done!")