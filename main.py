import os
import argparse
import re
import reddit_pull, text_to_speech, social_media_poster, video_processor

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
        text_to_speech.tts(mp3, selftext)

        #create video
        video_title = video_processor.audio_on_video(mp3, video_file, start)

        #delete mp3
        os.remove(f"data/mp3_downloads/{mp3}.mp3")
        os.remove(f"data/subtitles/{mp3}.srt")

        #upload.run(f"data/final_video/{video_title}.mp4")

        


def main(): 

    args = arg_handler()
    
    posts = reddit_pull.reddit_main(args[0], args[1])  

    video = post_convert(posts, args[2], args[3])


    



if __name__ == '__main__':
    main()


