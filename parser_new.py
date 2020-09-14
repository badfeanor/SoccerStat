from bs4 import BeautifulSoup
import requests
import psycopg2
import sys
from prettytable import PrettyTable
import imgkit

dbpass = sys.argv[1]

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')
ligasFetch = conn.cursor()
ligasFetch.execute("select * from metadata.parser_info;")
liga_dates = ligasFetch.fetchall()

for i in liga_dates:
    globals()[i[0]] = i[1]

ligas_names = []
for i in liga_dates:
    ligas_names.append(i[0])

for liga in ligas_names:
    print(liga)
    r = requests.get(globals()[liga]['url'], headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.body.find('table', attrs={'class': 'stat-table table'})
    rows = table.find_all("tr")
    data = []
    team = 'NO TEAM'
    for row in rows:
        cols = row.find_all("td")
        for col in cols:
            for a in col.findAll("a", href=True):
                team = str(a['href'])[22:-1].replace('-', '_')
                print(team)
        cols = [ele.text.strip() for ele in cols]
        team_stat = []
        for ele in cols:
    	    team_stat.append(ele)
        team_stat.append(team)
        data.append(team_stat)
    del data[0]
    print (data)

    InsData = conn.cursor()
    InsData.execute("TRUNCATE table " + liga + ".champ_stat;")
    InsData.executemany("INSERT INTO " + liga + ".champ_stat VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", data)
    conn.commit()

    table_pretty = PrettyTable()
    table_pretty.field_names = ["#", "Команда", "И", "В", "Н", "П", "МЗ", "МП", "О"]
    for i in data:
        del i[-1]
        table_pretty.add_row(i)
    html = table_pretty.get_html_string()
    # tf = tempfile.NamedTemporaryFile(dir='tmp', mode='w+b', delete=False, suffix='.png')
    css = ['/opt/SoccerStat/css.css']
    options = {'width': 385, 'disable-smart-width': '', 'encoding': "UTF-8", 'format': 'png'}
    imgkit.from_string(html, '/opt/SoccerStat_metadata/' + liga + '/champ_stat.png', options=options, css=css)

conn.close()