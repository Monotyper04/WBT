import telebot
import pickle

ver = "1.0 alpha"

num = 1

try:
    bot = telebot.TeleBot("942896002:AAHltM0-YNvCYQhawGuBLOXorRu0KhHpBxY")
    print("Запуск Бота :3")
except:
    print("Не верный ключ Телеграм Бота")
    pass

try :
    idList = open(r"ids.txt",'rb')
    ids = pickle.load(idList)
    idList.close()
except :
    print("Exeption : files not created")

for num in range(len(ids)):
    bot.send_message(ids[num], "Привет ! Я снова работаю , напиши мне что-нибудь))")
