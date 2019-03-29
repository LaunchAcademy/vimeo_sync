# VimeoSync

Upload videos to Vimeo from the command line

* `vimeo_converter` - command-line script to convert .mov files to a format that is more acceptable to Vimeo (minimizes Vimeo's processing time)
* `vimeo_sync.py` - python app to upload a video via Vimeo's API

## Setup
1. Install ffmpeg and python/pip from `requirements.txt`: `pip install -r requirements.txt`
* Set up a Vimeo API account and Access Token, giving yourself full access rights.
  * Run `cp .env.example .env` to create an `.env` file
  * Get the credentials from Vimeo or another team member and save in `.env`

## Instructions
* Convert from .mov to .mp4: `./vimeo_converter filename.mov`
* Upload to Vimeo: `python vimeo_sync.py filename.mp4 "My Video"`
