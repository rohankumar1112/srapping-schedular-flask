# http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion
# http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion/
# http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion

from flask import Flask
import schedule
import time
from bs4 import BeautifulSoup as bs
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pymongo
from datetime import datetime,date
import threading




app = Flask(__name__)

Heading =[]
urgent =[0,0,0]
status =[1,1,1]



def scrapLockbit():
    with TorBrowserDriver("/home/rohan/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
        time.sleep(6)
        driver.get("http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion")
    
    
        time.sleep(25)
        r =driver.page_source
        data ="".join(r)
        soup =bs(data,'html.parser')  

        heading =soup.find_all('div',class_='post-title')
        date =soup.find_all('div',class_='updated-post-date')
        para =soup.find_all('div',class_='post-block-text')
        link =soup.find_all('div',class_='post-block')


        web_links = soup.select('a') 

        actual_web_links = [web_link['href'] for web_link in web_links] 

        

        
        Date =[]
        Para =[]
        Body =[]
        Link =[]
        now=datetime.now()
        CreatedDate =now.strftime("%D")
            
        for i in heading:
            try:
                Heading.append(i.text)
            except:
                Heading.append("No Data")    

        for j in date:
            try:
                Date.append(j.text) 
            except:
                date.append("No Data")    

        for k in para:
            try:
                Para.append(k.text) 
            except:
                Para.append("No Data")  

        for l in link:
            try:
                Link.append(l.text)
            except:
                Link.append("No Data")            


        body = [i + j for i, j in zip(Heading, Para)]
        Body=str(body)

        Link1 ="http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion"


        df = pd.DataFrame({'title':Heading,'date':Date,'body':Body,'url':Link1,'createdAt':CreatedDate,'createdBy':"rohan kumar"})
        df.to_csv('/home/rohan/Desktop/schedular/Data.csv',index=False)

        print("LockBit Scrapping Done!!")



        # if __name__ =="__main__":
        #     print("Connecting to mongo...")
        #     client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
        #     print(client)
        #     db =client['webScraping']
        #     collection =db['rohantest']
        #     for i in range(len(Heading)):
        #         dictionary ={'title':Heading[i],'date':Date[i],'body':Heading[i]+Para[i],'url':Link1,'createdAt':CreatedDate,'createdBy':"rohan kumar"}
        #         collection.insert_one(dictionary)
        #     print("Data Inserted!!")
        driver.close()   
    Heading.clear()


def scrapHiveleak():
    with TorBrowserDriver("/home/rohan/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:

        time.sleep(6)
        driver.get("http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion/")
    
    
        time.sleep(20)
        r =driver.page_source
        data ="".join(r)
        soup =bs(data,'html.parser')       
        date =driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div/section/div/div[1]/div[2]/div[2]/p/span[1]')                                   
        para =driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div/section/div/div[1]/div[1]/p')
        head =driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div/section/div/div[1]/div[1]/h2')
        link =driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/section/div/div[1]/div[1]/ul/li[1]/a')
                                                                    
        print
        # Heading=[]
        Date=[]
        Para=[]
        Link =[]

    
        for i in head:
            try:
                Heading.append(i.text)
            except:
                Heading.append("No Data")

        for j in para:
            try:
                Para.append(j.text)  
            except:
                Para.append("No Data")    

        for k in date:
            try:
                Date.append(k.text) 
            except:
                Date.append("No Data")  

        for l in head:
            try:
                website_link =l.get_attribute('href')
                Link.append(website_link)
            except:
                Link.append("http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion/")              


        now=datetime.now()
        CreatedDate =now.strftime("%D")
        # CreatedDate =now.strftime("%D %H:%M:%S")
        Link1="http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion/"


       
        body = [i + j for i, j in zip(Heading, Para)]
        Body=str(body)

        df = pd.DataFrame({'title':Heading,'date':Date,'body':Body,'url':Link1,'createdAt':CreatedDate,'createdBy':"rohan kumar"})
        df.to_csv('/home/rohan/Desktop/schedular/Data2.csv',index=False)

        print("Hiveleak Scrapping Done!!")
        # if __name__ =="__main__":
        #     print("Connecting to mongo...")
        #     client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
        #     print(client)
        #     db =client['webScraping']
        #     collection =db['rohantest']
        #     for i in range(len(Heading)):
        #         dictionary ={'title':Heading[i],'date':Date[i],'body':Heading[i]+Para[i],'url':Link1,'createdAt':CreatedDate,'createdBy':"rohan kumar"}
        #         collection.insert_one(dictionary)
        #     print("Data Inserted!!")
        driver.close()   
    Heading.clear()
        

def scrapRansome():
    with TorBrowserDriver("/home/rohan/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:


            time.sleep(6)
            driver.get("http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion")

            time.sleep(20)


            r =driver.page_source
            data ="".join(r)
            soup =bs(data,'html.parser')  
            # next =driver.find_element(By.XPATH,'/html/body/main/div/nav/div/a[3]/span[2]')
            try:
                element = driver.find_element(By.XPATH,"/html/body/main/div/nav/div/a[3]/span[2]")
                element.click()
            except:
                print("Not Working...")    

            head =soup.find_all('h2')
            para =soup.find_all('p')
            link =soup.find_all('a')  

            print(link)                        
        
            # Heading=[]
            Para=[]
            Link =[]

        
            for i in head:
                try:
                    Heading.append(i.text)
                except:
                    Heading.append("No Data")

            for j in para:
                try:
                    Para.append(j.text)  
                except:
                    Para.append("No Data")    

            # for l in link:
            #         try:
            #             website_link =l.get_attribute('href')
            #             Link.append(website_link)
            #         except:
            #             Link.append("No data")    


            for k in head:
                try:
                    Link.append(k.get_attribute('href'))
                except:
                    Link.append("No Data") 


            body = [i + j for i, j in zip(Heading, Para)]
            Body=str(body)        

            now=datetime.now()
            CreatedDate =now.strftime("%D")

            Link1 ="http://ransomocmou6mnbquqz44ewosbkjk3o5qjsl3orawojexfook2j7esad.onion"



            df = pd.DataFrame({'Title': Heading, 'Body': body,'Link':Link1, 'Date-Created':CreatedDate})
            df.to_csv('/home/rohan/Desktop/schedule/11lineData.csv',index=False)
            
            print("Ransome Scrapping Done!!")



            # if __name__ =="__main__":
            #     print("Connecting to mongo...")
            #     client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
            #     print(client)
            #     db =client['webScraping']
            #     collection =db['rohantest']

            #     count = db.collection.count()

            #     if (count == 0):
            #         print("The collection is empty")
            #     else:
                    
                

            #         for i in range(len(Heading)):
            #             dictionary ={'title':Heading[i],'date':"No data",'body':Heading[i]+Para[i],'url':Link1,'createdAt':CreatedDate,'createdBy':"rohan kumar"}
            #             collection.insert_one(dictionary)
            #         print("Data Inserted!!")

            driver.close()   
    Heading.clear()



if len(Heading)==0:
    for i in range(2):
        if urgent[i] ==1:
            if i==0:
                schedule.every(1).minutes.do(scrapLockbit)
            else:
                schedule.every(1).minutes.do(scrapHiveleak)

    for j in range(2):
        if status[j] ==1:
            if j==0:
                schedule.every(1).minutes.do(scrapLockbit)

            else:
                schedule.every(1).minutes.do(scrapHiveleak)                


# Schedular Calling
def main():
    print("Working")
    while True:
        schedule.run_pending()
     


# Threading 
p1 =threading.Thread(target =main,args=())
p1.start()


@app.route('/')

def hello_world():
	return 'Hello Rohan!!'


# main driver function
if __name__ == '__main__':
	app.run()
