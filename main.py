from src.timeklis import apstrada_datni, apstrada_lapu
from pprint import pprint
import re

 
# html = apstrada_datni("dati/piemers.html")

# pprint(html.head.title.text)
# pprint(html.body.h2)
# pprint(html.body.p)
# pprint(html.find_all('p'))
# pprint(html.find_all(id=True))
# pprint(html.find_all(id="viens"))
# pprint(html.find_all("p", class_="teksts"))

# html = apstrada_lapu("https://www.tvnet.lv")
# pprint(html.head.title.text)
# raksti = html.find_all('a', class_="list-article__url")
# print(len(raksti))
# print(raksti[0])
#raksti = html.find_all('a', class_="list-article__url", string=re.compile("Latv")) # izvada tikai kur ir vārds `Latv`
#raksti = html.find_all('a', class_="list-article__url") # izvada visus ierakstus
# raksti = html.find_all('a', class_="list-article__url", string=re.compile("Covid-19"))
# for r in raksti:
#     print(r.text)

# idejas - ss.lv skripts automašīnu atlasai
#   vai arī dzīvokļa iegādei
#   interneta veikala cenas var salīdzināt precēm

# patstāvīgais darbs
html = apstrada_lapu("https://preili.lv/pasvaldiba/kontaktinformacija/strukturu-iestazu-darbinieku-kontakti/")
pprint(html.head.title.text)
