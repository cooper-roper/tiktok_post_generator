# TikTok Post Generator

Pull Reddit Posts, convert to captions, lay over video clips

## Development Setup

- Install ImageMagick

```bash
$ brew install ImageMagick
```

- Initialize Python v3.10 Virtual Environment

```bash
$ pip3 install virtualenv
$ python3 -m venv .env .
$ source .env/bin/activate
```

- Get Reddit API Secret Key, Reddit App ID, Reddit App Name, Reddit Username, and Reddit Password. Set environment variables `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`, `REDDIT_USERNAME`, & `REDDIT_PASSWORD` in file `.env/vars.env`. See [official documentation](https://code.visualstudio.com/docs/python/environments#_environment-variables) for more information on how to set up an environment file.

- Get Leopard SDK API Key, set environment variables `LEOPARD_ACCESS_KEY` & `AUDIO_PATH` in file `.env/vars.env`.

- Install Python dependencies

```bash
$ pip install -r requirements.txt
```

## Usage

Command Arguments:

```bash
$ run.py

-r      --subreddits    Subreddits to be used
-l      --limit         How many posts per subreddit
-v      --video-file    Target video file
-s      --start         Start duration of the audio file, default is 0
```

Example:

```bash
$ python run.py -r confessions -l 1

Posts grabbed...

Converting "Reddit_Post_Title" to mp3
Success

Processing Reddit_Post_Title to video...
Using test.mov

Moviepy - Building video data/final_videos/Reddit_Post_Title.mp4.
MoviePy - Writing audio in temp-audio.m4a
MoviePy - Done.                                                                                                                                                                                                                     
Moviepy - Writing video data/final_videos/Reddit_Post_Title.mp4
```
