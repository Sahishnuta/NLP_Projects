from gtts import gTTS
import base64

def text_to_speech(data):
    my_text = data
    tts = gTTS(text=my_text, lang='en', slow=False)
    tts.save('converted-file.mp3')
    with open("converted-file.mp3", "rb") as file:
        my_string = base64.b64encode(file.read())
    return my_string
