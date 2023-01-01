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

def arg_handler():
    parser = argparse.ArgumentParser(description="Python script automate tiktok posts")
    parser.add_argument("-r", "--subreddits", type=str, nargs='+', help='subreddits to be used')
    parser.add_argument("-l", "--limit", help="how many posts per subreddit", default=1, type=int)
    parser.add_argument("-v", "--video-file", help="Target video file")
    parser.add_argument("-s", "--start", help="Start duration of the audio file, default is 0", type=int)
    
    args = parser.parse_args()

    # If no input is provided, display the 'help' output and quit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    subreddits = args.subreddits
    limit = args.limit
    video_file = args.video_file
    start = args.start

    return [subreddits, limit, video_file, start]

    

def post_convert(posts, video_file, start):

    for post in posts:

        #title and body of post
        mp3 = str(post.title)
        selftext = str(post.selftext)

        #replace spaces and remove weird chars for title
        mp3 = mp3.replace(" ", "_")
        mp3 = re.sub(r'\W+', '', mp3)
    
        #create mp3 file
        audio.tts(mp3, selftext)

        #create video
        video_title = video.audio_on_video(mp3, video_file, start)

        #delete mp3
        os.remove(f"data/audio/{mp3}.mp3")
        os.remove(f"data/subtitles/{mp3}.srt")

        #upload.run(video_title)

        


def main(): 

    args = arg_handler()
    
    posts = reddit.reddit_main(args[0], args[1])  

    video_object = post_convert(posts, args[2], args[3])


    



if __name__ == '__main__':
    main()


