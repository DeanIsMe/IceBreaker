import telepot
import time
from telepot.loop import MessageLoop
import random

randnumber = random.randint(10000, 99999)
bot = telepot.Bot('679545486:AAEbCBdedlJ1lxFXpN1a-J-6LfgFQ4cAp04')
file = open("definitions.py", "w")
print("Please send " + str(randnumber) + "to the bot")

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == str(randnumber):
        file.write("userId = " + str(chat_id))
        print(chat_id)
        print("got user id")
        file.close()
    print(command)
    
    
    


MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)



    
