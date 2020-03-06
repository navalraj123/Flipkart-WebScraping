from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
driver = webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
for i in range (1,12):
    url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&sort=price_asc&page="+str(i)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating=a.find('div', attrs={'class':'hGSR34'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text) 
        
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('miproducts.csv', index=False, encoding='utf-8')        
