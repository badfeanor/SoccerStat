from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

dbpass = sys.argv[1]

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                        port='5432')

england = {'schema_name': 'england', 'url': 'https://www.sports.ru/football/match/england/'}

name_of_liga = england['schema_name']
l = requests.get(england['url'])
soup_l = BeautifulSoup(l.content, 'html.parser')
table = soup_l.body.find('table', attrs={'class': 'stat-table table'})
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    for col in cols:
        for a in col.findAll("a", href=True):
            team = str(a['href'])[22:-1].replace('-', '_')
            print(team)
            r = requests.get(a['href'] + 'stat/')
            soup = BeautifulSoup(r.text, 'html.parser')
            table = soup.body.find('table', attrs={'class': 'stat-table sortable-table js-active'})
            rows = table.find_all("tr")
            data = []
            for row in rows:
                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
            del data[0]
            del data[-1]
            for player in data:
                curConf = conn.cursor()
                curConf.execute("TRUNCATE table " + name_of_liga + "." + team + "_players;")
                sql_script = "INSERT INTO " + name_of_liga + "." + team + "_players VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                curConf.executemany(sql_script, player)
                conn.commit()
conn.close()
