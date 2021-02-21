from gtts import gTTS
import os
txt = open("Lorem Ipsum.txt")
myText = txt.read()

language = "en";
output = gTTS(text=myText,lang=language, slow=False)
output.save("output.mp3")
txt.close()
os.system("start output.mp3")
