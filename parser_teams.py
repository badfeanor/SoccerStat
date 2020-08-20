from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

dbpass = sys.argv[1]

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
    l = requests.get(globals()[liga]['url'])
    curConf = conn.cursor()
    curConf.execute("TRUNCATE table " + liga + ".teams CASCADE;")
    conn.commit()
    soup_l = BeautifulSoup(l.content, 'html.parser')
    table_l = soup_l.body.find('table', attrs={'class': 'stat-table table'})
    rows_l = table_l.find_all("tr")
    data = []
    for row_l in rows_l:
        cols_l = row_l.find_all("td")
        for col_l in cols_l:
            for a in col_l.findAll("a", href=True):
                team = str(a['href'])[22:-1].replace('-', '_')
                team_cyrillic = a.text
                data = [str(team), str(team_cyrillic)]
                print(data)
                curConf = conn.cursor()
                curConf.execute("INSERT INTO " + liga + ".teams VALUES ('" + str(team) + "', '" + str(team_cyrillic) + "');")
                conn.commit()
conn.close()
