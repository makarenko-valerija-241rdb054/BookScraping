import requests
import bs4

url="https://www.amazon.com/kindle-dbs/storefront?storeType=browse&node=154606011"
saturs=requests.get(url)

print(saturs.status_code)

if saturs.status_code==200:
    lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
    #print(lapa)
    atrada=lapa.find_all("body")
    print(atrada)
    f=open("temp.txt", "w")
    for a in atrada:
        print(a)
    f.close()

