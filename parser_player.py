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
    name_of_liga = globals()[liga]['schema_name']
    print(name_of_liga)
    l = requests.get(globals()[liga]['url'])
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
                table2 = soup.body.find('table', attrs={'class': 'stat-table sortable-table js-active'})
                rows = table2.find_all("tr")
                data = []
                for row in rows:
                    cols = row.find_all("td")
                    cols = [ele.text.strip() for ele in cols]
                    data.append([ele for ele in cols if ele])
                del data[0]
                del data[-1]
                for i in data:
                    for idx, item in enumerate(i):
                        if item == '–':
                            i[idx] = '0'
                curConf = conn.cursor()
                curConf.execute("CREATE TABLE IF NOT EXISTS " + name_of_liga + "." + team + "_players (number smallint, name varchar(30), played smallint, min smallint, bz smallint, vnz smallint, goals smallint, pen smallint, p smallint, gp smallint, yc smallint, rc smallint);")
                curConf.execute("TRUNCATE table " + name_of_liga + "." + team + "_players;")
                sql_script = "INSERT INTO " + name_of_liga + "." + team + "_players VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                curConf.executemany(sql_script, data)
                conn.commit()
conn.close()

