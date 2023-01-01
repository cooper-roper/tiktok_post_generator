import os
import sys
import praw
from dotenv import load_dotenv

# Import from parent directory
# https://stackoverflow.com/a/30536516
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import dotenv_path

# Load environment variables for Reddit authentication
load_dotenv(dotenv_path)


# Returns a praw.Reddit object
def reddit_auth():
    return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        password=os.getenv('REDDIT_PASSWORD'),
        user_agent=os.getenv('REDDIT_USER_AGENT'),
        username=os.getenv('REDDIT_USERNAME'))


# Pull the latest 'limit' amount of posts from each subreddit 
# in the list 'subreddits'
def post_pull(subreddits, limit):
	reddit_api = reddit_auth()
	
	subreddits_posts = []
	for sub in subreddits:
		subreddit = reddit_api.subreddit(sub)
		posts = subreddit.top(time_filter="day", limit=limit)
		subreddits_posts.append(posts)

	print("Posts grabbed.\n") 
	return posts