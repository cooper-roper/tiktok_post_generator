import os
import sys
import praw
from dotenv import load_dotenv

# Import from parent directory
# https://stackoverflow.com/a/30536516
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import dotenv_path

load_dotenv(dotenv_path)

# returns a  praw.Reddit object
def praw_oauth():
    return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        password=os.getenv('REDDIT_PASSWORD'),
        user_agent=os.getenv('REDDIT_USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'))


def reddit_main(subreddits, limit):
	reddit_api = praw_oauth()
	
	subreddits_posts = []
	for sub in subreddits:
		subreddit = reddit_api.subreddit(sub)
		posts = subreddit.top(time_filter="day", limit=limit)
		subreddits_posts.append(posts)

	print("Posts grabbed.\n") 
	return posts