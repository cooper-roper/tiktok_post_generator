import re
import os
import sys
from gtts import gTTS


language = 'en'


def tts(title, contents):
	print(f"Converting post \"{title}\" to TTS .mp3 file")
  
	# Parse the text into a format ready for turning into an audio file
	contents = f"{title}. {contents}"
	re.sub(r'http\S+', '', contents)
	contents = contents.replace("_", " ")
	  
	# Convert sanitized text to TTS object & save to an audio file
	tts_obj = gTTS(text=contents, lang=language, slow=False)
	try:
		tts_obj.save(f"{os.getcwd()}/data/audio/{title}.mp3")
		print("Success\n")
	except Exception as e:
		print(f"Failed to save .mp3 for Reddit post. Error information:\n{e}")
		sys.exit(1)

