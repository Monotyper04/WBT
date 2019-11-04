import telebot
import pyowm
import random
import pickle
from telebot import types

markup = types.ReplyKeyboardMarkup()

ver = "1.1 beta"

nic = ['624303728']

ugadayNum = 0

try:

    nickList = open(r"database.txt",'rb')
    nicks = pickle.load(nickList)
    nickList.close()

    owm = pyowm.OWM('5ea6afa4aef8afab6cb9663b48fe4148', language= 'ru')
    bot = telebot.TeleBot("942896002:AAHltM0-YNvCYQhawGuBLOXorRu0KhHpBxY")
    print("Запуск Бота :3")

except:

    nickList = open(r"database.txt",'wb')
    pickle.dump(nic, nickList)
    nickList.close()

    print("Не верный ключ Телеграм Бота или нехватает файлов")
    pass

print("Бот запушен" , ver , "\nLogs : \n\n")


@bot.message_handler(commands=['start'])
def send_start(message):

    markup = types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, message.text , reply_markup = markup)

    markup = types.ReplyKeyboardMarkup()

    try:
        nickList = open(r"database.txt",'rb')
        nicks = pickle.load(nickList)
        nicks.index(message.from_user.first_name + message.from_user.last_name)
    except:
        nickList = open(r"database.txt",'rb')
        nicks = pickle.load(nickList)
        nickList.close()
        nickList = open(r"database.txt",'wb')
        nicks.append(message.from_user.first_name + message.from_user.last_name)
        pickle.dump(nicks, nickList)

    markup.row('/help')

    answer = "Вас приветствует бот Monotyper \n /help для помощи \n\nСсылка на мой канал : https://www.youtube.com/channel/UCvMJkoR0xSjFNtYIK22bCUg"

    bot.send_message(message.chat.id, answer , reply_markup = markup)

    print("\n\nstarting", "\n\nfrom" , message.from_user.first_name , "||")

    @bot.message_handler(commands=['help'])
    def send_help(message):

        markup = types.ReplyKeyboardRemove()

        bot.send_message(message.chat.id, message.text , reply_markup = markup)

        markup = types.ReplyKeyboardMarkup()

        markup.row('/weather', '/games')
        markup.row('/ЖдатьОбновлений😄', '/ЖдатьМоеВидео')

        answer = "Это бета версия моего бота которому я буду добавлять разные функции" + "\n\nВерсия бота : " + ver
        answer += "\n\n  Доступные команды : \n /weather \n /games"
        answer += "\n\n В будущем будет больше команд"


        bot.send_message(message.chat.id, answer , reply_markup = markup)



        print("\n\nhelping" , "\n\nfrom" , message.from_user.first_name , "||")

    @bot.message_handler(commands=['ЖдатьМоеВидео'])
    def send_waitVideo(message):
        try :
            idList = open(r"ids.txt",'rb')
            ids = pickle.load(idList)
            idList.close()
            try:
                idList = open(r"ids.txt",'rb')
                ids = pickle.load(idList)
                ids.index(message.chat.id)

                answer = "Вы уже зарегестрированы , ждите видео\n/start"

                bot.send_message(message.chat.id, answer)
            except:
                idList = open(r"ids.txt",'rb')
                ids = pickle.load(idList)
                idList.close()
                idList = open(r"ids.txt",'wb')
                ids.append(message.chat.id)
                pickle.dump(ids, idList)

                answer = "Спасибо что ждёте 😄\n/start"

                bot.send_message(message.chat.id, answer)
        except :
            answer = "Попробуйте ещё раз пожалуйста(Приношу свои извинения)\n\nError:500 Internal Server Error \n/start"

            bot.send_message(message.chat.id, answer)

            print("Exeption : files not created \n Now is created")
            idList = open(r"ids.txt",'wb')
            pickle.dump(nic , idList)
            idList.close()




    @bot.message_handler(commands=['ЖдатьОбновлений😄'])
    def send_wait(message):

        markup = types.ReplyKeyboardRemove()

        answer = "Я рад что кто-то ждет обновлений😉 \n/start"

        bot.send_message(message.chat.id, answer , reply_markup = markup)

        print("\n\nwaiting" , "\n\nfrom" , message.from_user.first_name , "||")

    @bot.message_handler(commands=['games'])
    def send_games(message):
        markup = types.ReplyKeyboardRemove()

        bot.send_message(message.chat.id, message.text , reply_markup = markup)

        markup = types.ReplyKeyboardMarkup()

        markup.row('/kosti')
        markup.row('/ЖдатьОбновлений😄')

        answer = "Выберите игру : \n\n"
        answer += "/kosti - генерирует число от 1 до 6\n"
        bot.send_message(message.chat.id,answer,reply_markup = markup)
        print("\n\ngames" , "\n\nfrom" , message.from_user.first_name , "||")

        @bot.message_handler(commands=['/kosti'])
        def send_kosti(message):
            rNum = random.randrange(1,7,1)
            bot.send_message(message.chat.id,"У вас выпало : " + str(rNum))
            print("\n\nkosti" , rNum , "\n\nfrom" , message.from_user.first_name , "||")

    @bot.message_handler(commands=['weather'])
    def send_weather(message):

        print("\n\nweather" , "\n\nfrom" , message.from_user.first_name , "||")


        bot.send_message(message.chat.id,"Введите название города")
        try:
            @bot.message_handler(content_types=['text'])
            def send_weatherMess(message):

                try:
                    observation = owm.weather_at_place( message.text )
                    w = observation.get_weather()
                    temp = w.get_temperature('celsius')["temp"]

                    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
                    answer += "Температура сейчас в районе : " + str(round(temp)) + "\n"

                    if temp < 10:
                        answer += "\nДовольно холодно , оденся потеплее"
                    elif temp < 20:
                        answer += "\nПрохладно , надо что-то на себя накинуть"
                    else:
                        answer += "\nДовольно тепло , одевайся как хочешь"

                    bot.send_message(message.chat.id, answer)
                    print( "\n\n" + "Запрос : " , message.text , "\n\nfrom" , message.from_user.first_name , "||")


                except:
                    pass


        except:
            print( "\n\nExeption", message.text , "\n\nfrom" , message.from_user.first_name , "||")

            answer = "Твоя команда \" " + message.text + " \" не найден(а)"

            bot.send_message(message.chat.id, answer)



bot.polling( none_stop = True)