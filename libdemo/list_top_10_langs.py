# List top 10 programming lang from tiobe.com

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.tiobe.com/tiobe-index")
contents = resp.text

bs = BeautifulSoup(contents, "html.parser")
table = bs.find(id="top20")  # find table with id top20
if table is None:
    print('Sorry! Could not get table!')
    exit()

body = table.find("tbody")
rows = body.find_all("tr")
for row in rows[:10]:
    cols = row.find_all("td")
    name = cols[4].text
    rating = float(cols[5].text[:-1])
    print(f"{name:20}  {rating:5.2f}")

