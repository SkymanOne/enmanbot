import telebot
from telebot import types
from token_const import token

bot = telebot.TeleBot(token)  # token file ignored


@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text == 'Главное меню✅')
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Расписание⏱', 'Контакты📞')
    markup.row('Справки📝', 'FAQ💡')
    bot.send_message(message.from_user.id,
                     'Приветствую, что тебя интересует?',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Расписание⏱')
def schedule(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('1 курс', '2 курс')
    markup.row('3 курс', '4 курс')
    markup.row('Главное меню✅')
    bot.send_message(message.from_user.id, 'Выбери курс',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Контакты📞')
def contacts(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Деканат', 'Преподаватели')
    markup.row('Студ. Центр EnMan')
    markup.row('Главное меню✅')
    bot.send_message(message.from_user.id, 'С кем хотите связаться?',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Деканат')
def deanery(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Серебреннико', 'Харитонов', 'Стуловский')
    markup.row('Мильчаков', 'Мурзагареев', 'Максименкова')
    markup.row('Алексеева', 'Фролова', 'Контакты📞')
    bot.send_message(message.from_user.id, 'Список деканата',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Преподаватели')
def teachers(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Математика', 'Психология')
    markup.row('Философия', 'Экономическая теория')
    markup.row('Менеджмент', 'История', 'Английский')
    markup.row('Контакты📞')
    bot.send_message(message.from_user.id, 'Выбери предмет',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Справки📝')
def references(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Заказать справку')
    markup.row('Справка об обучени')
    markup.row('Главное меню✅')
    bot.send_message(message.from_user.id, 'Доступные справки',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'FAQ💡')
def faq(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('О факультете', 'Для студента')
    markup.row('Для абитуриента')
    markup.row('Главное меню✅')
    bot.send_message(message.from_user.id, 'Что тебе инетерсно?',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Для студента')
def for_student(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Как сделать справку для военкомата')
    markup.row('FAQ💡')
    bot.send_message(message.from_user.id, 'Вот руководства для студента',
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Для абитуриента')
def for_student(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Какие документы нужны для поступления', 'Проходные баллы')
    markup.row('Какие предметы сдавать', 'FAQ💡')
    bot.send_message(message.from_user.id, 'Вот руководства для студента',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_mes(message: types.Message):
    bot.send_message(message.from_user.id, 'Я не понимаю, что ты написал, попробуй еще раз.',
                     reply_to_message_id=message.message_id)


bot.polling(True)
