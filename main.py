import telebot
import random



bot = telebot.TeleBot('6523416756:AAHOOrzXq35PnIX07vv0j3Shj1PZMnliOp8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я заебался,но вроде сделал! Кидай число от 1 до 10" )

@bot.message_handler(content_types=['text'])
def text_handler(message):
    User_answer = message.text.lower()
    chat_id = message.chat.id
    Bot_number = str(random.randint(1, 10))
    bot.send_message(chat_id, f'Загаданное число: {Bot_number}')
    bot.send_message(chat_id, f'Число игрока: {User_answer}')
    if User_answer == Bot_number:
        bot.send_message(chat_id, "Угадал!")
    else:
        bot.send_message(chat_id, "ЛОХ! ПОПУСК! НЕ УГАДАЛ!")


bot.infinity_polling()

