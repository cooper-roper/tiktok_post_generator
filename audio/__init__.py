import re
import os
import sys
import pyttsx3


language = 'en'


def tts(title, contents):
	print(f"Converting post \"{title}\" to TTS .mp3 file")
  
	# Parse the text into a format ready for turning into an audio file
	contents = f"{title}. {contents}"
	re.sub(r'http\S+', '', contents)
	re.sub(r'[^A-Za-z0-9 ?!".,]+', '', contents)

	subs = "AITA"

	replace = "Am I the a-hole"	

	# replace string and ignore casing
	compiled = re.compile(re.escape(subs), re.IGNORECASE)
	contents = compited.sub(replace, contents)

	contents = contents.replace("_", " ")

	#convert sanitized text
	engine = pyttsx3.init()
	engine.setProperty('rate', 250)

	try:
		engine.save_to_file(contents, f"{os.getcwd()}/data/audio/{title}.mp3")
		engine.runAndWait()
		print("Success\n")
	except Exception as e:
		print(f"Failed to save .mp3 for Reddit post. Error information:\n{e}")
		sys.exit(1)

