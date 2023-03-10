from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import pvleopard
from typing import *
import os, random


def audio_on_video(title, video_file, start):
	print(f"Processing {title} to video.")

	# Random video if none provided
	if not video_file:
		video_file = random_video()

	# Load the audio
	audio_clip = AudioFileClip(f"data/audio/{title}.mp3")

	# Load the video
	video_clip = VideoFileClip(f"data/videos/{video_file}")

	# Load the subtitles
	subtitles = subtitle_handler(title, video_clip.size)

	
	# Create start time and end
	if not start:
		start = random.randrange(int(video_clip.end - audio_clip.end) - 1)
	end = start + audio_clip.end + 3

	# Clipped and set audio
	clipped = video_clip.subclip(start, end).set_audio(audio_clip)

	# Add subtitles
	final_clip = CompositeVideoClip([clipped, subtitles.set_position(('center'))])

	# Create video
	final_clip.write_videofile(f"data/final_videos/{title}.mp4", 
					 codec='libx264', 
					 audio_codec='aac', 
					 temp_audiofile=f"data/audio/temp-audio.m4a",
					 remove_temp=True)

	print(f"{title} now available\n")


def subtitle_handler(audio_clip, size):
	# Generating closed caption file (srt file)
	leopard = pvleopard.create(access_key=os.getenv('LEOPARD_ACCESS_KEY'))
	transcript, words = leopard.process_file(f"data/audio/{audio_clip}.mp3")

	with open(f'data/subtitles/{audio_clip}.srt', 'w') as f:
		f.write(to_srt(words))

	generator = lambda txt: TextClip(txt, font='Helvetica', fontsize=68, color='white', size=size, method='caption')
	subtitles = SubtitlesClip(f'data/subtitles/{audio_clip}.srt', generator) 

	return subtitles

def second_to_timecode(x: float) -> str:
	hour, x 	= divmod(x, 3600)
	minute, x 	= divmod(x, 60)
	second, x 	= divmod(x, 1)
	millisecond = int(x * 1000.)

	return '%.2d:%.2d:%.2d,%.3d' % (hour, minute, second, millisecond)

def to_srt(
		words: Sequence[pvleopard.Leopard.Word],
		endpoint_sec: float = 1.,
		length_limit: Optional[int] = 16) -> str:

	def _helper(end: int) -> None:
		lines.append("%d" % section)
		lines.append("%s --> %s" % (
				second_to_timecode(words[start].start_sec),
				second_to_timecode(words[end].end_sec)))
		lines.append(' '.join(x.word for x in words[start:(end + 1)]))
		lines.append('')

	lines 	= list()
	section = 0
	start 	= 0
	for k in range(1, len(words)):
		if ((words[k].start_sec - words[k - 1].end_sec) >= endpoint_sec) or \
				(length_limit is not None and (k - start) >= length_limit):
			_helper(k - 1)
			start = k
			section += 1
	_helper(len(words) - 1)

	return '\n'.join(lines)



def random_video():
	videos = os.listdir("data/videos")
	videos.remove('README.md')
	
	video_file = random.choice(videos) #change dir name to whatever

	print(f"Using {video_file}\n")

	return video_file

