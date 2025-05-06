import requests
import bs4
import re
import time
from openpyxl import Workbook

###
###Linked list data structure!
###
# node
class Node:
    def __init__(self, code, name, danger):
        self.code=code
        self.name=name
        self.danger=danger
        self.next=None
# the list itself
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
    
    #method for printing out the items
    def print(self):
        curr=self.head
        while(curr):
            print(str(curr.code)+"---"+str(curr.name)+"---"+str(curr.danger))
            curr=curr.next



def main():
    #the Linked List which will store all the items that will be scraped from the web
    SCPList=LinkedList()
    url="https://scp-wiki.wikidot.com/"
    saturs=requests.get(url)

    #check if the url response is valid
    if saturs.status_code==200:
        lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
        #find all hyperlinks using Beautiful Soup
        atrada=lapa.find_all("a")
        #write the hyperlinks into a text file ("temp.txt")
        #this is done for the purpose of debugging - to see that all the hyperlinks are indeed found
        f=open("temp.txt", "w")
        for a in atrada:
            f.write(str(a)+"\n")
        f.close()
        #read the hyperlinks from the resulting file
        f=open("temp.txt", "r")
        lines=f.readlines()
        #now the task is to find the rightmost text fragment behind the slash on the hyperlinks that contain Roman numerals
        #that way we get a list of links to different SCP libraries (li)
        li=[]
        for l in lines:
            x=re.search("^<a href=\".+\">(I|II|III|IV|V|VI|VII|VIII|IX)</a>", l) #searching using regex library
            if x:
                y=l.split("\"")
                z=re.sub("/", "", y[1])
                li.append(str(url+z))#this way a new url is made from the url of the current page and the fragment extracted
                #it can later be used with the requests library

        #asking the user to specify the SCP catalogue of interest
        print("Which SCP catalogue would you like to study? (roman numerals I-IX)")
        use=input()
        #asking the user to specify the number of objects they would like to find
        print("How many would you like to find?")
        use2=input()
        #this match case determines which link from "li" will be used based on the catalogue selected
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
        #the new url is used with the requests library
        saturs=requests.get(url1)
        #url check
        if saturs.status_code==200:
            lapa=bs4.BeautifulSoup(saturs.content, "html.parser")
            #finding all list items using Beautiful Soup (each SCP object is a list item)
            atrada=lapa.find_all("li")
            #yet again, for debugging purposes, the items are written into a file
            f=open("temp2.txt", "w")
            for a in atrada:
                #list items that are SCPs have child hyperlinks - this clause finds them
                link=a.find_all("a")
                link1=link[0]
                x=re.search(r"^SCP-\d+$", link1.contents[0])#a regex function call to determine if hyperlink text
                #corresponds to an SCP title
                if x:
                    #first linked list value - code!
                    code=link1.contents[0]
                    #second linked list value - name!
                    name=a.contents[1]
                    #extracting the value under a href tag of a hyperlink
                    tag=bs4.BeautifulSoup(str(link1), "html.parser").a
                    rel=tag["href"]
                    rel1=re.sub("/", "", rel)
                    #a time buffer not to overload the server
                    time.sleep(2)
                    #opening a web page of an SCP item to scrape the danger class
                    saturs2=requests.get(url+rel1)
                    if saturs2.status_code==200:
                        lapa=bs4.BeautifulSoup(saturs2.content, "html.parser")
                        #the danger class comes under the tag "strong"
                        atrada=lapa.find_all("strong")
                        for a in atrada:
                            x=re.search("^Object Class:$", str(a.contents[0]))#looking for the indicator that the html
                            #tag "strong" that was found was indeed the danger class
                            if x:
                                par=a.find_parent("p")
                                #third linked list value - danger!
                                danger=par.contents[1]
                                SCPList.append(code, name, danger) #adding the value to the list
                                #Monitoring the WebScraping process
                                print("Found "+str(SCPList.size)+" SCPs")
                #the size buffer
                if SCPList.size>=int(use2):
                    break
            #beginning of the command terminal
            print("All desired SCPs have been found!")
            print("Type print n (for example print 10) to display an element of database on screen")
            print("Type print all to display all database on screen")
            print("Type excel class (for example excel keter) to get a spreadsheet of SCPs belonging to a danger class")
            print("Type exit to exit the terminal")
            terminal=True
            while(terminal):
                use=input()
                #command indicator for printing a particular item (with index)
                x=re.search(r"^print \d+$", use)
                #command indicator for printing all items
                y=re.search("^print all$", use)
                #command indicator for making an excel file with items of a danger class
                z=re.search("^excel (safe|euclid|keter|thaumiel)$", use)
                #command indicator for exiting the terminal
                w=re.search("^exit$", use)
                #print item
                if x:
                    use1=re.sub("print ", "", use)
                    index=int(use1)
                    print(SCPList.search(index).code+"---"+SCPList.search(index).name+"---"+SCPList.search(index).danger)
                #print all items
                if y:
                    SCPList.print()
                #make excel file
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
                #exit    
                if w:
                    terminal=False
                    
            

            
if __name__ == "__main__":
    main()            
