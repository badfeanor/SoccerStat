from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

dbpass = sys.argv[1]

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')

england = {'schema_name': 'england', 'url': 'https://www.sports.ru/football/match/england/'}
spain = {'schema_name': 'spain', 'url': 'https://www.sports.ru/football/match/spain/'}
italy = {'schema_name': 'italy', 'url': 'https://www.sports.ru/football/match/italy/'}
germany = {'schema_name': 'germany', 'url': 'https://www.sports.ru/football/match/germany/'}


for liga in england, spain, italy, germany:
    # print(liga['url'])
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
    # print(data)

    curConf = conn.cursor()
    curConf.execute("TRUNCATE table " + name_of_liga + ".champ_stat;")
    curConf.executemany("INSERT INTO " + name_of_liga + ".champ_stat VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", data)
    conn.commit()
conn.close()
