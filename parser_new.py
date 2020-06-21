from bs4 import BeautifulSoup
import requests
import psycopg2
import sys
from prettytable import PrettyTable
import imgkit

dbpass = sys.argv[1]

conn = psycopg2.connect(dbname='soccer_stat', user='soccer', password=dbpass, host='127.0.0.1',
                            port='5432')
list_of_ligas =[]
ligasFetch = conn.cursor()
ligasFetch.execute("select distinct schema_name from information_schema.schemata where schema_name != 'public' and schema_name != 'pg_catalog' and schema_name != 'information_schema';")
list_of_ligas = ligasFetch.fetchall()
conn.close()


england = {'schema_name': 'england', 'url': 'https://www.sports.ru/football/match/england/'}
spain = {'schema_name': 'spain', 'url': 'https://www.sports.ru/football/match/spain/'}
italy = {'schema_name': 'italy', 'url': 'https://www.sports.ru/football/match/italy/'}
germany = {'schema_name': 'germany', 'url': 'https://www.sports.ru/football/match/germany/'}


for liga in list_of_ligas:
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
    print(data)
conn.close()
