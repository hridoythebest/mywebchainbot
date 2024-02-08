import telebot
from telebot import types

bot = telebot.TeleBot('6367524435:AAESoUf8oFMCdGcnWG0ZvDE8a1V_5MkkHok')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_use_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Hello to you too", parse_mode='html')
#     elif message.text == 'id': 
#          bot.send_message(message.chat.id, f"Your id is: {message.from_user.id}", parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('Cards.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#          bot.send_message(message.chat.id, "Write a proper message!", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message): 
    bot.send_message(message.chat.id, 'Wow, cool photo')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Main Website", url="https://hub-fas.com/"))
    markup.add(types.InlineKeyboardButton("Education Website", url="https://hub-university.com/"))
    bot.send_message(message.chat.id, 'Start learning now!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Start learning now!', reply_markup=markup) 


bot.polling(none_stop=True)