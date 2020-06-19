from PIL import Image, ImageDraw, ImageFont
from beautifultable import BeautifulTable
import imgkit


data = [['1', 'Ювентус', '26', '20', '3', '3', '50', '24', '63'], ['2', 'Лацио', '26', '19', '5', '2', '60', '23', '62'], ['3', 'Интер', '25', '16', '6', '3', '49', '24', '54'], ['4', 'Аталанта', '25', '14', '6', '5', '70', '34', '48'], ['5', 'Рома', '26', '13', '6', '7', '51', '35', '45'], ['6', 'Наполи', '26', '11', '6', '9', '41', '36', '39'], ['7', 'Милан', '26', '10', '6', '10', '28', '34', '36'], ['8', 'Верона', '25', '9', '8', '8', '29', '26', '35'], ['9', 'Парма', '25', '10', '5', '10', '32', '31', '35'], ['10', 'Болонья', '26', '9', '7', '10', '38', '42', '34'], ['11', 'Сассуоло', '25', '9', '5', '11', '41', '39', '32'], ['12', 'Кальяри', '25', '8', '8', '9', '41', '40', '32'], ['13', 'Фиорентина', '26', '7', '9', '10', '32', '36', '30'], ['14', 'Удинезе', '26', '7', '7', '12', '21', '37', '28'], ['15', 'Торино', '25', '8', '3', '14', '28', '45', '27'], ['16', 'Сампдория', '25', '7', '5', '13', '28', '44', '26'], ['17', 'Дженоа', '26', '6', '7', '13', '31', '47', '25'], ['18', 'Лечче', '26', '6', '7', '13', '34', '56', '25'], ['19', 'СПАЛ', '26', '5', '3', '18', '20', '44', '18'], ['20', 'Брешия', '26', '4', '4', '18', '22', '49', '16']]

table = BeautifulTable()
table.set_style(BeautifulTable.STYLE_COMPACT)
table.column_headers = ["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"]
table.column_alignments['Команда'] = BeautifulTable.ALIGN_LEFT
for i in data:
    table.append_row(i)
table_str = table.get_string()

# table = PrettyTable(["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"])
# table.padding_width = 1 # One space between column edges and contents (default)
# for i in data:
#     table.add_row(i)
# table_str = table.get_string()

# table_str = tabulate(data, headers=["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"], tablefmt="simple")

with open('output.txt','w') as file:
    file.write(table_str)

options = {
    'format': 'png',
    'crop-h': '3',
    'crop-w': '3',
    'crop-x': '3',
    'crop-y': '3',
    'encoding': "UTF-8",
    'no-outline': None
}

imgkit.from_url(table_str, 'out.png', options=options)

# img = Image.new('RGB', (240, 320), color=(73, 109, 137))
# font = ImageFont.truetype("arial.ttf", 10, encoding='unic')
# d = ImageDraw.Draw(img)
# d.text((10,10), table_str, fill=(255,255,0), font=font)
# img.save('table.png')