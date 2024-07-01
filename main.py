import telebot
from telebot import types
TOKEN = '6642468718:AAFLbN7L6_gMd_iDufD9E6U9L6pvb7U4H38'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('Наши соц сети', callback_data='social_platforms'))
    bot.send_message(message.chat.id, 'Выберете варианты', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'social_platforms':
        show_social(call.message,call.id)
    elif call.data == 'back_to_menu':
        send_welcome(call.message)
def show_social(message,call_id):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('VK',url = 'https://trello.com/b/B8cRro0r/type-soul-info-v2'))
    markup.add(types.InlineKeyboardButton('YouTube', url = 'https://www.youtube.com'))
    markup.add(types.InlineKeyboardButton('instagram', url = 'https://www.youtube.com/watch?v=S3izA5BA-gE'))
    markup.add(types.InlineKeyboardButton('Назад',callback_data='back_to_menu'))
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Вот все наши соцсети',reply_markup=markup)

def get_back_to_menu(message):
    markup = types.InlineKeyboardMarkup()    
    markup.add(types.InlineKeyboardButton('Наши соц сети', callback_data='social_platforms'))
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Выберете варианты',reply_markup=markup)
if __name__ == '__main__':
    bot.polling(none_stop=True)