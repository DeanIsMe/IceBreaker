#telegram_bot.py
import telepot
from definitions import IbConfig
import time
import pyttsx3 as pyttsx
import os
import speech_recognition as sr
from gtts import gTTS
from telepot.loop import MessageLoop

langTag = IbConfig['listenLanguage'] # for listening only
bot = telepot.Bot(IbConfig['telepotToken'])


credJson = ''
if IbConfig['googleServiceKeyFile']:
    with open(IbConfig['googleServiceKeyFile'], 'r') as credFile:
        credJson = credFile.read()

if not credJson:
    print('Google Cloud Service Key not supplied. Requests may be rejected')
    print('File name given in config: <{}>'.format(IbConfig['googleServiceKeyFile']))

def echoCb(recog, audioData):
    timeSec = len(audioData.frame_data) / (audioData.sample_rate * audioData.sample_width)
    print('Detected ({} seconds):'.format(timeSec))
    try:
        if credJson:
            text = recog.recognize_google_cloud(audio_data = audioData, credentials_json = credJson, language=langTag)
        else:
            # No service key supplied
            text = recog.recognize_google(audioData, language=langTag)
        print(text)
        print(str(IbConfig['telepotChatId']))
        bot.sendMessage(str(IbConfig['telepotChatId']), text)
    except:
        print("Fehler")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == '/start':
        tts = gTTS(text=IbConfig['startMessage'], lang=langTag)
    else:
        tts = gTTS(text=command, lang=IbConfig['speakLanguage'])
    tts.save("textToSpeech.mp3")
    os.system("mpg321 textToSpeech.mp3")

print('Starting Listening')
r = sr.Recognizer()
myMic = sr.Microphone(device_index=IbConfig['micDeviceIndex'], sample_rate=16000, chunk_size=1024)
stopListening = r.listen_in_background(source=myMic, callback=echoCb, phrase_time_limit=5)

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)

input("Press enter key to end...")
print("Ending...")
stopListening(True)
print("Finished")

    
