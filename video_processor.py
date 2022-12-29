from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import pvleopard
from typing import *
import os, random
from dotenv import load_dotenv


def audio_on_video(title, video_file, start):

	print(f"Processing {title} to video...")

	#random video if none provided
	if not video_file:
		video_file = video_processor.random_video()

	# load the audio
	audio_clip = AudioFileClip(f"mp3_downloads/{title}.mp3")

	# load the video
	video_clip = VideoFileClip(f"videos/{video_file}")

	subtitles = subtitle_handler(title, video_clip.size)

	
	#create start time and end
	if not start:
		start = random.randrange(int(video_clip.end - audio_clip.end) - 1)
	end = start + audio_clip.end + 3

	#clipped and set audio
	clipped = video_clip.subclip(start, end).set_audio(audio_clip)

	#add subtitles
	final_clip = CompositeVideoClip([clipped, subtitles.set_position(('center'))])

	#create video
	final_clip.write_videofile(f"final_video/{title}.mp4", 
                     codec='libx264', 
                     audio_codec='aac', 
                     temp_audiofile='temp-audio.m4a', 
                     remove_temp=True)

	print(f"{title} now available\n")


def subtitle_handler(audio_clip, size):

	#generating closed caption file (srt file)
	leopard = pvleopard.create(access_key=os.getenv('LEOPARD_ACCESS_KEY'))
	transcript, words = leopard.process_file(f"mp3_downloads/{audio_clip}.mp3")

	with open(f'subtitles/{audio_clip}.srt', 'w') as f:
		f.write(to_srt(words))

	generator = lambda txt: TextClip(txt, font='Helvetica', fontsize=72, color='white', size = size, method='caption')
	subtitles = SubtitlesClip(f'subtitles/{audio_clip}.srt', generator) 

	return subtitles

def second_to_timecode(x: float) -> str:
    hour, x = divmod(x, 3600)
    minute, x = divmod(x, 60)
    second, x = divmod(x, 1)
    millisecond = int(x * 1000.)

    return '%.2d:%.2d:%.2d,%.3d' % (hour, minute, second, millisecond)

def to_srt(
        words: Sequence[pvleopard.Leopard.Word],
        endpoint_sec: float = 1.,
        length_limit: Optional[int] = 16) -> str:
    def _helper(end: int) -> None:
        lines.append("%d" % section)
        lines.append(
            "%s --> %s" %
            (
                second_to_timecode(words[start].start_sec),
                second_to_timecode(words[end].end_sec)
            )
        )
        lines.append(' '.join(x.word for x in words[start:(end + 1)]))
        lines.append('')

    lines = list()
    section = 0
    start = 0
    for k in range(1, len(words)):
        if ((words[k].start_sec - words[k - 1].end_sec) >= endpoint_sec) or \
                (length_limit is not None and (k - start) >= length_limit):
            _helper(k - 1)
            start = k
            section += 1
    _helper(len(words) - 1)

    return '\n'.join(lines)



def random_video():

	video_file = random.choice(os.listdir("videos")) #change dir name to whatever

	print(f"Using {video_file}\n")

	return video_file

