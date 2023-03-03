import time
import telebot
from telebot import types
from config import*
bot=telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, 'WARNING! YOU TEXTED IN WRONG AREA FOOL')   #shit pants
    time.sleep(1)
    bot.send_message(message.chat.id,'14')
    time.sleep(1)
    bot.send_message(message.chat.id, '13')
    time.sleep(1)
    bot.send_message(message.chat.id, '12')           #scary countdown
    time.sleep(1)
    bot.send_message(message.chat.id, '11')
    time.sleep(1)
    bot.send_message(message.chat.id, '10')
    time.sleep(1)
    bot.send_message(message.chat.id, '9')
    time.sleep(1)
    bot.send_message(message.chat.id, '8')
    time.sleep(1)
    bot.send_message(message.chat.id, 'БАНННННННННН!!!!!!!!!!!') #murder
    bot.kick_chat_member(user_id=message.from_user.id,chat_id=message.chat.id)

bot.polling()
