from bs4 import BeautifulSoup
import requests
import psycopg2
import sys
from prettytable import PrettyTable
import imgkit

dbpass = sys.argv[1]

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')

england = {'schema_name': 'england', 'url': 'https://www.sports.ru/football/match/england/'}
spain = {'schema_name': 'spain', 'url': 'https://www.sports.ru/football/match/spain/'}
italy = {'schema_name': 'italy', 'url': 'https://www.sports.ru/football/match/italy/'}
germany = {'schema_name': 'germany', 'url': 'https://www.sports.ru/football/match/germany/'}


for liga in england, spain, italy, germany:
    name_of_liga = liga['schema_name']
    print(name_of_liga)
    r = requests.get(liga['url'])
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.body.find('table', attrs={'class': 'stat-table table'})
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    del data[0]

    table_pretty = PrettyTable()
    table_pretty.field_names = ["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"]
    for i in data:
        table_pretty.add_row(i)
    html = table_pretty.get_html_string()
    # tf = tempfile.NamedTemporaryFile(dir='tmp', mode='w+b', delete=False, suffix='.png')
    css = ['css.css']
    options = {'width': 380, 'disable-smart-width': '', 'encoding': "UTF-8", 'format': 'png'}
    imgkit.from_string(html, '/opt/SoccerStat_metadata/' + name_of_liga + '/champ_stat.png', options=options, css=css)

    curConf = conn.cursor()
    curConf.execute("TRUNCATE table " + name_of_liga + ".champ_stat;")
    curConf.executemany("INSERT INTO " + name_of_liga + ".champ_stat VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", data)
    conn.commit()
conn.close()
