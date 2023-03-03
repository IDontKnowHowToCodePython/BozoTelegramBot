
import telebot
import wikipedia

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi im bozo bot using wikipedia sex')
@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        result = wikipedia.summary(message.text)
        bot.send_message(message.chat.id, result)
    except:
        bot.send_message(message.chat.id, 'Error')

bot.polling()