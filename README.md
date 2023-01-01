# TikTok Post Generator

Pull Reddit Posts, convert to captions, lay over video clips

## Installation

- Get Reddit API Secret Key, Reddit App ID, Reddit App Name, Reddit Username, and Reddit Password. Set environment variables `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`

- Get Leopard SDK API Key, set environment variables `ACCESS_KEY`, `AUDIO_PATH`

- Set up Python v3.10 Virtual Environment

```bash
pip3 install virtualenv
python3 -m venv .env .
source .env/bin/activate
```

- Install Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

Command Arguments:

```text
-r      --subreddits    Subreddits to be used
-l      --limit         How many posts per subreddit
-v      --video-file    Target video file
-s      --start         Start duration of the audio file, default is 0
```
