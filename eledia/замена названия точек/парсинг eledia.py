import requests
from bs4 import BeautifulSoup



poins_d = {}
def get_response(url):
    response = requests.get(url)
    return response


def get_points(r):
    text, link = r.text, f"https://www.eledia.ru{r['href']}"
    res  = get_response(link)
    soup = BeautifulSoup(res.text, 'lxml').find_all('div', {'class':'eTitle'})
    print(text, link)
    for i in soup:
        a = i.find('a')
        name = a.text.split()[0]
        url = f"https://www.eledia.ru{a['href']}"
        # print(name, url)
        poins_d[name] = url

    #     print(i.text, i['href'])
    # r =  requests.get(link)
    # print(r)
    # return r


r = get_response('https://www.eledia.ru/publ/16')
soup = BeautifulSoup(r.text, 'lxml').find_all('a', {"class": "catName"})

for r in soup[3:5]:

    if 'Дополнительные материалы' in r :
        continue
    # print(r)
    points = get_points(r)
print(poins_d)