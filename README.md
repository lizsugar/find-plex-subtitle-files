# Description

This project downloads an entire show's video and subtitle files from any Plex server the user's Plex account has access to.

This is designed to build the entire library folder structure needed for [Knowledge Seeker](https://github.com/lizsugar/knowledge-seeker).  

A third component that builds Knowledge Seeker's requisite json file is planned.

# Steps
1. Configure plex_config.py (see plex_config.SAMPLE.py)
2. Run `plex_subtitles.py "<SHOW NAME>"` - for example: `plex_subtitles.py "The Legend of Korra"`
3. Wait for it to finish

# TODO
- [ ] Any sort of error handling (e.g. when the show title is mistyped)
- [ ] If the script is run twice with two different shows, create separate libraries for them
- [ ] Clean up script further and standardize on variable naming (camelCase vs using_underscores)