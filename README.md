# VimeoSync

Upload videos to Vimeo from the command line

* `vimeo_converter` - command-line script to convert .mov files to a format that is more acceptable to Vimeo (minimizes Vimeo's processing time)
* `vimeo_sync.py` - python app to upload a video via Vimeo's API

## Setup

* install ffmpeg and python/pip
* `pip install -r requirements.txt`
* Set up a Vimeo API account and Access Token, giving yourself full access rights.
* `cp .env.example .env`
* Store your credentials in `.env`

## Instructions
* `./vimeo_converter filename.mov`
* `python vimeo_sync.py filename.mp4 "My Video"`
