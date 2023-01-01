from gtts import gTTS
import re
import os

def tts(title, selftext):

	print(f"Converting \"{title}\" to mp3")
  
	language = 'en'

	selftext = title + ". " + selftext

	re.sub(r'http\S+', '', selftext)

	selftext = selftext.replace("_", " ")
	  
	myobj = gTTS(text=selftext, lang=language, slow=False)
	
	myobj.save(f"{os.getcwd()}/data/audio/{title}.mp3")

	print("Success\n")

