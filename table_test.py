# необходимо установить wkhtmltopdf и добавить переменные окружения при необходимости

from prettytable import PrettyTable
import imgkit
import tempfile

path_wkthmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)

data = [['1', 'Ювентус', '26', '20', '3', '3', '50', '24', '63'],
        ['2', 'Лацио', '26', '19', '5', '2', '60', '23', '62'],
        ['3', 'Интер', '25', '16', '6', '3', '49', '24', '54'],
        ['4', 'Аталанта', '25', '14', '6', '5', '70', '34', '48'],
        ['5', 'Рома', '26', '13', '6', '7', '51', '35', '45'],
        ['6', 'Наполи', '26', '11', '6', '9', '41', '36', '39'],
        ['7', 'Милан', '26', '10', '6', '10', '28', '34', '36'],
        ['8', 'Верона', '25', '9', '8', '8', '29', '26', '35'],
        ['9', 'Парма', '25', '10', '5', '10', '32', '31', '35'],
        ['10', 'Болонья', '26', '9', '7', '10', '38', '42', '34'],
        ['11', 'Сассуоло', '25', '9', '5', '11', '41', '39', '32'],
        ['12', 'Кальяри', '25', '8', '8', '9', '41', '40', '32'],
        ['13', 'Фиорентина', '26', '7', '9', '10', '32', '36', '30'],
        ['14', 'Удинезе', '26', '7', '7', '12', '21', '37', '28'],
        ['15', 'Торино', '25', '8', '3', '14', '28', '45', '27'],
        ['16', 'Сампдория', '25', '7', '5', '13', '28', '44', '26'],
        ['17', 'Дженоа', '26', '6', '7', '13', '31', '47', '25'],
        ['18', 'Лечче', '26', '6', '7', '13', '34', '56', '25'],
        ['19', 'СПАЛ', '26', '5', '3', '18', '20', '44', '18'],
        ['20', 'Брешия', '26', '4', '4', '18', '22', '49', '16']]


# x = PrettyTable()
# x.field_names = ["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"]

# for i in data:
#    x.add_row(i)

# html = x.get_html_string()

# with open('test.html', 'w') as f:
#    f.write(x.get_html_string())


def getTableImg(champ):
    # conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
    #                        port='5432')
    # curConf = conn.cursor()
    # curConf.execute("SELECT * FROM " + champ + ";")
    # table_list = curConf.fetchall()
    # conn.close()
    table_list = data
    table = PrettyTable()
    table.field_names = ["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"]
    for i in table_list:
        table.add_row(i)
    html = table.get_html_string()
    tf = tempfile.NamedTemporaryFile(dir='tmp', mode='w+b', delete=False, suffix='.png')
    css = ['css.css']
    options = {'width': 320, 'disable-smart-width': '', 'encoding': "UTF-8", 'format': 'png'}
    imgkit.from_string(html, tf.name, config=config, options=options, css=css)
    return print(tf.name)


getTableImg(champ=1)

# def ger(bot, update):
#     print('Кто-то хочет Германию')
#     my_keyboard = ReplyKeyboardMarkup([['/england', '/italy'], ['/spain', '/germany']])  # добавление кнопок
#     img = open(getTableImg("england.champ_stat"), 'rb')
#     bot.send_photo(photo=img), reply_markup=my_keyboard)
#     bot.message.reply_photo(photo=img).format(bot.message.chat), reply_markup=my_keyboard)
