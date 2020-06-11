from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

dbpass = sys.argv[1]

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')

epl = {'table_name': 'epl', 'url': 'https://www.football-stat.ru/football/competition/1026'}
ell = {'table_name': 'ell', 'url': 'https://www.football-stat.ru/football/competition/1030'}
isa = {'table_name': 'isa', 'url': 'https://www.football-stat.ru/football/competition/1056'}
gbl = {'table_name': 'gbl', 'url': 'https://www.football-stat.ru/football/competition/1032'}


for liga in epl, ell, isa, gbl:
    # print(liga['url'])
    name_of_liga = liga['table_name']
    print(name_of_liga)
    r = requests.get(liga['url'])
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.body.find('table', attrs={'class': 'table table-sm'})
    rows = table.find_all("tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    del data[0]
    for i in data:
        i[-1] = i[-1].replace('\n\n\n', '')
    # print(data)

    curConf = conn.cursor()
    curConf.execute("TRUNCATE table " + name_of_liga + ";")
    curConf.executemany("INSERT INTO " + name_of_liga + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", data)
    conn.commit()
conn.close()
