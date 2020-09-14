from bs4 import BeautifulSoup
import requests
import psycopg2
import sys

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
    name_of_liga = globals()[liga]['schema_name']
    print(name_of_liga)
    curConf = conn.cursor()
    curConf.execute("TRUNCATE table " + name_of_liga + ".players;")
    conn.commit()
    l = requests.get(globals()[liga]['url'], headers = headers)
    soup_l = BeautifulSoup(l.content, 'html.parser')
    table_l = soup_l.body.find('table', attrs={'class': 'stat-table table'})
    rows_l = table_l.find_all("tr")
    for row_l in rows_l:
        cols_l = row_l.find_all("td")
        for col_l in cols_l:
            for a in col_l.findAll("a", href=True):
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
                for i in data:
                    i.insert(2, team)
                    for idx, item in enumerate(i):
                        if item == '–':
                            i[idx] = '0'
                curConf = conn.cursor()
                curConf.execute("CREATE TABLE IF NOT EXISTS " + name_of_liga + ".players (number smallint, name varchar(30), team varchar(30), played smallint, min smallint, bz smallint, vnz smallint, goals smallint, pen smallint, p smallint, gp smallint, yc smallint, rc smallint);")
                sql_script = "INSERT INTO " + name_of_liga + ".players VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                curConf.executemany(sql_script, data)
                conn.commit()
conn.close()
