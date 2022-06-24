from scrapper import getJokes
import json
import telebot
from datetime import datetime

with open('key.json','r') as keyFile:
    key = json.load(keyFile)['API_KEY'] #For more api_key security

ChuckBot = telebot.TeleBot(key)

@ChuckBot.message_handler(commands=["start"])
def returnHelp(message):
    ChuckBot.reply_to(message,"""
    This ChuckBot was created by Effi Bello.
    You may enter anything and Chuck will answer accordingly.
    Enter a number between 1-101 in order to get one of his jokes
    (Chuck wouldn't appreciate if you'd be pushing his limits).
    You can also ask for the time by using /time. """)    

@ChuckBot.message_handler(commands=["time"])   
def returnTime(message):
    time = datetime.now()
    time = time.strftime("%H") + ':' + time.strftime("%M")
    ChuckBot.send_message(message.chat.id,"Chuck Norris doesn't need a watch, he knows the time is " + time + '.')
   

@ChuckBot.message_handler(content_types=['text'])
def returnJoke(message):
    greets = ["hello","hey","hi","greetings"] #Replying to certain keywords
    for greet in greets:
        if greet in message.text.lower():
            ChuckBot.send_message(message.chat.id,"Chuck Norris doesn't say " + greet + ', ' + greet + " says Chuck Norris")
            break
    else:
        try:
            if int(message.text) in range(1,102): 
                jokeNumber = int(message.text)
                ChuckBot.reply_to(message, str(jokeNumber) +'. '+ getJokes(jokeNumber))
            elif int(message.text) <= 0:
                ChuckBot.reply_to(message,"Be positive and give me a positive number!")
            else:
                ChuckBot.reply_to(message,"Slow down Cowboy, i've got only 101 jokes for now.")           
        except:
            ChuckBot.reply_to(message, "Although im Chuck Norris, I can only tell you a joke if you give me a number between 1-101")

ChuckBot.polling()
