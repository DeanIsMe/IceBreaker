import telepot
from definitions import user
import time
import pyttsx
import os
import speech_recognition as sr
from gtts import gTTS
from telepot.loop import MessageLoop

userId = user()
langTag = "de_DE"
bot = telepot.Bot('679545486:AAEbCBdedlJ1lxFXpN1a-J-6LfgFQ4cAp04')

def echoCb(recog, audioData):
    timeSec = len(audioData.frame_data) / (audioData.sample_rate * audioData.sample_width)
    print('Detected ({} seconds):'.format(timeSec))
    try:
        text = recog.recognize_google(audioData, language=langTag)
        print(text)
        print(str(userId))
        bot.sendMessage(str(userId), text)
    except:
        print("Fehler")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == '/start':
        tts = gTTS(text="Hallo, ich bin unsere dolmetschende Eule. Stelle mich bitte auf deine Handflaeche und ich sage dir, was dein tauber Gegenueber schreibt. Wenn du etwas sagst, teile ich das deinem Gegenueber mit", lang='de')
    else:
        tts = gTTS(text=command, lang='de')
    tts.save("test.mp3")
    os.system("mpg321 test.mp3")
    
r = sr.Recognizer()
myMic = sr.Microphone(device_index=0, sample_rate=16000, chunk_size=1024)
stopListening = r.listen_in_background(source=myMic, callback=echoCb, phrase_time_limit=5)


MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)

input("Press enter key to end...")
print("Ending...")
stopListening(True)
print("Finished")

    
