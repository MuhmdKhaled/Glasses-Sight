from PIL import Image
from pytesseract import image_to_string
from playsound import playsound
import gtts

image=Image.open('Intermediate-essay-excerpt-2-791x1024.jpg')
text=image_to_string(image,lang='eng')
tts=gtts.gTTS(text,lang='en',slow='false')
tts.save('voice.mp3')
playsound('voice.mp3')