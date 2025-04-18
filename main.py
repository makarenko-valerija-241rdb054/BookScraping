import requests
import bs4
import re
import time
from openpyxl import Workbook


class Node:
    def __init__(self, code, name, danger):
        self.code=code
        self.name=name
        self.danger=danger
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self, code, name, danger):
        node=Node(code, name, danger)
        if self.size==0:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1
        return True
    
    def search(self, index):
        if index>self.size or index<=0:
            return None
        if index==self.size:
            return self.tail
        if index<self.size and index>1:
            temp=self.head
            iter=1
            while(iter<index):
                temp=temp.next
                iter+=1
            return temp
        if index==1:
            return self.head
    
    def print(self):
        curr=self.head
        while(curr):
            print(str(curr.code)+"---"+str(curr.name)+"---"+str(curr.danger))
            curr=curr.next



def main():
    SCPList=LinkedList()
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

        print("Which SCP catalogue would you like to study? (roman numerals I-IX)")
        use=input()
        print("How many would you like to find?")
        use2=input()
        match use:
            case "I":
                url1=li[0]
            case "II":
                url1=li[1]
            case "III":
                url1=li[2]
            case "IV":
                url1=li[3]
            case "V":
                url1=li[4]
            case "VI":
                url1=li[5]
            case "VII":
                url1=li[6]
            case "VIII":
                url1=li[7]
            case "IX":
                url1=li[8]
            case _:
                url1=li[1]
        saturs=requests.get(url1)
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
                x=re.search(r"^SCP-\d+$", link1.contents[0])
                if x:
                    #first linked list value - code!
                    code=link1.contents[0]
                    #second linked list value - name!
                    name=a.contents[1]
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
                                SCPList.append(code, name, danger)
                                #Monitoring the WebScraping process
                                print("Found "+str(SCPList.size)+" SCPs")
                if SCPList.size>=int(use2):
                    break
            print("All desired SCPs have been found!")
            print("Type print n (for example print 10) to display an element of database on screen")
            print("Type print all to display all database on screen")
            print("Type excel class (for example excel keter) to get a spreadsheet of SCPs belonging to a danger class")
            print("Type exit to exit the terminal")
            terminal=True
            while(terminal):
                use=input()
                x=re.search(r"^print \d+$", use)
                y=re.search("^print all$", use)
                z=re.search("^excel (safe|euclid|keter|thaumiel)$", use)
                w=re.search("^exit$", use)
                if x:
                    use1=re.sub("print ", "", use)
                    index=int(use1)
                    print(SCPList.search(index).code+"---"+SCPList.search(index).name+"---"+SCPList.search(index).danger)
                if y:
                    SCPList.print()
                if z:
                    dan=re.sub(r"excel ", "", use)
                    dan=dan.strip()
                    wb=Workbook()
                    name_string="SCP "+dan
                    ws1=wb.create_sheet(name_string, 0)
                    ws1.append(["Code", "Name", "Danger Class"])
                    curr=SCPList.head
                    while(curr):
                        if curr.danger.strip().lower()==dan:
                            ws1.append([curr.code, curr.name, curr.danger])
                        curr=curr.next
                    filename=f"{dan}_scp_list.xlsx"
                    wb.save(filename)
                    print("Excel file "+filename+" saved!")
                    
                if w:
                    terminal=False
                    
            

            
if __name__ == "__main__":
    main()            
