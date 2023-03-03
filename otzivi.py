import telebot
from telebot import types
from config import*
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['end'])
def start_message(message):
    bobo=types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Add feedback', request_contact=True)
    bobo.add(btn1)
    bot.send_message(message.chat.id, 'Thanks for buying, can u pls add feed back :3', reply_markup=bobo)

@bot.message_handler(content_types=['contact'])
def start_message(message):
    sent = bot.send_message(message.chat.id, 'OMG THX!!111 now pls add text u want to connect')
    a =str(message.contact.phone_number)
    b =message.contact.first_name
    c =message.contact.last_name
    bot.register_next_step_handler(sent, otzuv(message,a,b,c))

def otzuv(message,a,b,c):
    file=open('contact','a+',encoding='utf8')          #btw make a file that will store their contacts dumbass
    file.write('\n'+' '+a+' '+b+' '+c+' '+str(message.chat.id))
    file.close()
    #bot.edit_message_reply_markup(callback.message.chat.id,callback.message.message_id)
bot.infinity_polling()