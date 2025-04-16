import requests
import bs4
import re
import time

url="https://scp-wiki.wikidot.com/"
saturs=requests.get(url)

#print(saturs.status_code)
#f=open("temp.txt", "w")
#f.write(str(saturs.content))
#f.close()

if saturs.status_code==200:
    lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
    atrada=lapa.find_all("a")
    f=open("temp.txt", "w")
    for a in atrada:
        f.write(str(a)+"\n")
    f.close()
    f=open("temp.txt", "r")
    lines=f.readlines()
    li=[]
    for l in lines:
        x=re.search("^<a href=\".+\">(I|II|III|IV|V|VI|VII|VIII|IX)</a>", l)
        if x:
            y=re.split("\"", l)
            z=re.sub("/", "", y[1])
            li.append(str(url+z))
    #print(li)

    saturs=requests.get(li[1])
    if saturs.status_code==200:
        #f=open("temp2.txt", "w")
        #f.write(str(saturs.content))
        #f.close()
        lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
        atrada=lapa.find_all("li")
        f=open("temp2.txt", "w")
        for a in atrada:
            link=a.find_all("a")
            link1=link[0]
            #print(link1.contents)
            x=re.search("^SCP-\d+$", link1.contents[0])
            if x:
                tag=bs4.BeautifulSoup(str(link1), "html.parser").a
                rel=tag["href"]
                rel1=re.sub("/", "", rel)
                time.sleep(2)
                saturs2=requests.get(url+rel1)
                if saturs2.status_code==200:
                    lapa=bs4.BeautifulSoup(saturs2.content, "html.parser")
                    atrada=lapa.find_all("strong")
                    for a in atrada:
                        x=re.search("^Object Class:$", str(a.contents[0]))
                        if x:
                            par=a.find_parent("p")
                            danger=par.contents[1]

            
            
