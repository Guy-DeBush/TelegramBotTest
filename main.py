import telebot
from telebot import types
import random



bot = telebot.TeleBot('6523416756:AAHOOrzXq35PnIX07vv0j3Shj1PZMnliOp8')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кнопочка для игры")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я заебался,но вроде сделал!", reply_markup=markup)

@bot.message_handler(commands=['randnumber'])
def get_text_messages(message):
    if message.text == 'Кнопочка для игры':
        bot.send_message(message.from_user.id, 'Бот загадал число от 1 до 10, угадывай!') #ответ бота
        User_answer = message.chat.id
        YourNum = bot.send_message(User_answer, 'Твоё число:')
        bot.register_next_step_handler(YourNum, step_Set_Price)
        Bot_number = random.randint(1,10)
        if YourNum == Bot_number:
            bot.send_message(message.from_user.id,"Угадал!")
        else:
            bot.send_message(message.from_user.id,"ЛОХ! ПОПУСК! НЕ УГАДАЛ!")

def step_Set_Price(message):
    User_answer = message.chat.id
    userPrice= message.text

bot.polling(none_stop=True, interval=0)
