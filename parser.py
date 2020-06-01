from bs4 import BeautifulSoup
import requests
import json

r = requests.get('https://www.football-stat.ru/football/competition/1026')
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
    i[-1] = i[-1].replace('\n\n\n', ' ')
print(data)
#print(json.dumps(data, ensure_ascii=False, indent=4))

