# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = '260150114:AAGO75JwgWSYCMwWzeY1n93ki2GtTq_ukgk'
bot = telebot.TeleBot(TOKEN)

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            chat_id = str(m.chat.id)
            user_name = str(m.chat.first_name)
            user_text = m.text
            print user_name + " [" + chat_id + "]: " + user_text

bot.set_update_listener(listener)  # register listener

@bot.message_handler(commands=['hohi'])
def command_hiho(m):
    chat_id = m.chat.id
    bot.send_message(chat_id, 'petiso')

@bot.message_handler(commands=['quetemeto'])
def command_hiho(m):
    chat_id = m.chat.id
    bot.send_chat_action(chat_id, 'upload_photo')
    img = open('quetemeto.jpg', 'rb')
    bot.send_photo(chat_id, img)
    img.close()

@bot.message_handler(commands=['tranqui'])
def command_hiho(m):
    chat_id = m.chat.id
    bot.send_chat_action(chat_id, 'upload_photo')
    img = open('tranqui.jpg', 'rb')
    bot.send_photo(chat_id, img)
    img.close()

@bot.message_handler(commands=['ojala'])
def command_hiho(m):
    chat_id = m.chat.id
    bot.send_chat_action(chat_id, 'upload_photo')
    img = open('ojala.jpg', 'rb')
    bot.send_photo(chat_id, img)
    img.close()

# filter on a specific message
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_text_hi(m):
    if 'dios' in m.text:
        bot.send_message(m.chat.id, 'loooool')
    if 'hola' in m.text:
        bot.send_message(m.chat.id, 'hoooolaaaa')



bot.polling(none_stop = True)
