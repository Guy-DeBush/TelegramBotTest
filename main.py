import telebot
from telebot import types
import random



bot = telebot.TeleBot('6523416756:AAHOOrzXq35PnIX07vv0j3Shj1PZMnliOp8')

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.from_user.id, "Привет! Я заебался,но вроде сделал! Кидай число от 1 до 100" )
    User_answer = message.text
    Bot_number = random.randint(1, 10)
    if User_answer == Bot_number:
        bot.send_message(message.from_user.id, "Угадал!")
    else:
        bot.send_message(message.from_user.id, "ЛОХ! ПОПУСК! НЕ УГАДАЛ!")


bot.polling(none_stop=True, interval=0) #Можно написать и инфинити поллинг, но бля так саснее

