import telebot
from telebot import types
from token_const import token

bot = telebot.TeleBot(token)  # token file ignored


@bot.message_handler(content_types=['text'])
def echo_mes(message: types.Message):
    bot.send_message(message.from_user.id, 'Вот твое сообщение', reply_to_message_id=message.message_id)


bot.polling(True)
