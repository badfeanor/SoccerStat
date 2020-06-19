from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from beautifultable import BeautifulTable
import psycopg2
import os
os.environ.get('TOKEN')
token = os.environ.get('TOKEN')
dbpass = os.environ.get('DBPASS')

def getTable(champ):
    conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')
    curConf = conn.cursor()
    curConf.execute("SELECT * FROM " + champ + ";")
    table_list = curConf.fetchall()
    conn.close()
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_COMPACT)
    table.column_headers = ["#", "К", "И", "В", "Н", "П", "МЗ", "МП", "О"]
    table.column_alignments['К'] = BeautifulTable.ALIGN_LEFT
    for i in table_list:
        table.append_row(i)
    return str(table)

def sms(bot, update):
    print('Кто-то написал /start. Что мне делать?')
    my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']]) #добавление кнопок
    bot.message.reply_text('Привет, я футбольный бот! \nЯ пока ни хрена не умею! Но скоро научусь! \nЯ очень на это надеюсь, {}! \nА пока выбери какой чемпионат тебе интереснее....' .format(bot.message.chat.first_name), reply_markup=my_keyboard)

def eng(bot, update):
    print('Кто-то хочет Англию')
    my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']]) #добавление кнопок
#    bot.message.reply_text('ММММ! \n{}, да ты ценитель футбола с туманного Альбиона! Тогда лови. \n\n https://www.soccer.ru/tournament/england/table' .format(bot.message.chat.first_name), reply_markup=my_keyboard)
    bot.message.reply_text(getTable("england.champ_stat").format(bot.message.chat), reply_markup=my_keyboard)

def ger(bot, update):
    print('Кто-то хочет Германию')
    my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']])  # добавление кнопок
#    bot.message.reply_text('ОО! Я-я! \nА ты, {}, любитель брутального арийского фузбала!!! \n\n https://www.soccer.ru/tournament/germany/table' .format(bot.message.chat.first_name), reply_markup=my_keyboard)
    bot.message.reply_text(getTable("germany.champ_stat").format(bot.message.chat), reply_markup=my_keyboard)

def esp(bot, update):
    print('Кто-то хочет Испанию')
    my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']])  # добавление кнопок
#    bot.message.reply_text('Как оказалось, {}, ты у нас ещё один ценитель корриды и загорелых испанских мулаток! Тогда лови! \n\n https://www.soccer.ru/tournament/spain/table' .format(bot.message.chat.first_name), reply_markup=my_keyboard)
    bot.message.reply_text(getTable("spain.champ_stat").format(bot.message.chat), reply_markup=my_keyboard)

def ita(bot, update):
    print('Кто-то хочет Италию')
    my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']])  # добавление кнопок
#    bot.message.reply_text('Ох и не ожидал от тебя я такого, {}! \nЛюбуйся на здоровье \n\n https://www.soccer.ru/tournament/italy/table' .format(bot.message.chat.first_name), reply_markup=my_keyboard)
    bot.message.reply_text(getTable("italy.champ_stat").format(bot.message.chat), reply_markup=my_keyboard)

def main():
    my_bot = Updater(token, "https://api.telegram.org/bot", use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(CommandHandler('england', eng))
    my_bot.dispatcher.add_handler(CommandHandler('germany', ger))
    my_bot.dispatcher.add_handler(CommandHandler('spain', esp))
    my_bot.dispatcher.add_handler(CommandHandler('italy', ita))
    my_bot.start_polling()
    my_bot.idle()

main()
