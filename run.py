import os
import re
import sys
import argparse
import reddit, audio, video
#import upload


#global variables
subreddits = None
video_file = None
start = None

parser = argparse.ArgumentParser(description="Python script automate tiktok posts")


# Initialize parser object with arguments
def parser_init():
    parser.add_argument("-r", "--subreddits", type=str, nargs='+', help='subreddits to be used')
    parser.add_argument("-l", "--limit", help="how many posts per subreddit", default=1, type=int)
    parser.add_argument("-v", "--video-file", help="Target video file")
    parser.add_argument("-s", "--start", help="Start duration of the audio file, default is 0", type=int)


# Process user input, return help message if input is invalid
def input_handler():
    parser_init()

    # If no input is provided, display the 'help' output and quit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        return parser.parse_args()
    

def post_convert(posts, video_file, start):
    for post in posts:
        # Title and body of post
        mp3 = str(post.title)
        selftext = str(post.selftext)

        # Replace spaces and remove weird chars for title
        mp3 = mp3.replace(" ", "_")
        mp3 = re.sub(r'\W+', '', mp3)
    
        # Create mp3 file
        audio.tts(mp3, selftext)

        # Create video
        video_title = video.audio_on_video(mp3, video_file, start)

        # Delete mp3
        os.remove(f"data/audio/{mp3}.mp3")
        os.remove(f"data/subtitles/{mp3}.srt")

        #upload.run(video_title)


if __name__ == '__main__':
    args         = input_handler()
    posts        = reddit.post_pull(args.subreddits, args.limit)  
    video_object = post_convert(posts, args.video_file, args.start)