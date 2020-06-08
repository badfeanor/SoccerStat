from telegram.ext import Updater
from telegram.ext import CommandHandler

def sms(bot, update):
    print('Кто-то написал /start. Что мне делать?')
    bot.message.reply_text('Привет, {}! Я футбольный бот! \nЯ пока ни хрена не умею! Но скоро научусь! \nЯ очень на это надеюсь, ' .format(bot.message.chat.first_name))

def main():
    my_bot = Updater("1163071581:AAFE-lN_YbFxHsZMnJoN3Ht7qKC7pXb4-Q0", "https://telegg.ru/orig/bot", use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.start_polling()
    my_bot.idle()

main()