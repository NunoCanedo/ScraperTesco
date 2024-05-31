## Import Libraries

import SQLFunctions
import AuxFunctions
import ScrapeProductLink

import time
import datetime
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv


import undetected_chromedriver as uc


#driver = uc.Chrome()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

Tesco_Taxonomy = csv.DictReader(open("Tesco_Taxonomy.csv"))

#df = pd.read_csv('Tesco_Taxonomy', index_col=0)

#Tesco_Taxonomy.append(df)
#print(Tesco_Taxonomy)


## Function to accept cokkies

def click(selector):
       
    try:
        driver.find_element(By.XPATH, selector).click()
            
    except NoSuchElementException:
        return False


def next_page_link(x):
    
    try:
        link  = x.find('a', href=True)['href']
        return link
        
        
    except TypeError:
        return None
        



def next_page(data, soup):
    
    soup=BeautifulSoup(driver.page_source,'lxml')
    data = soup.select("#product-list > div.product-list-view.has-trolley > div.pagination-component.grid > nav > ul > li")
    
    for x in data:
    
        try:
            title  = x.find('a', title=True)['title']
            if title == 'Go to results page':   
                link =  x.find('a', href=True)['href']
                #print(link)
                return f'https://www.tesco.com{link}'       
            
        except TypeError:
            pass
    

def find_data(data, url):
    
    a = 10
    
    for item in data:
        
        product_data = {
            'extration_date': datetime.date.today(),
            'product_ID': AuxFunctions.product_code(url.get('aisle_ID'), a),
            'product_name': AuxFunctions.extract_data(item, 'span.styled__Text-sc-1i711qa-1'),
            'price': AuxFunctions.extract_data(item, 'p.styled__StyledHeading-sc-119w3hf-2'),
            'price_per': AuxFunctions.extract_data(item, 'p.styled__StyledFootnote-sc-119w3hf-7'),
            'club_card_price': AuxFunctions.extract_data(item, 'p.text__StyledText-sc-1jpzi8m-0'),
            'price_kg': AuxFunctions.extract_data(item, 'select'),
            'label': AuxFunctions.extract_data(item, 'span.ddsweb-tag__container'),
            'aldi_price_label': AuxFunctions.extract_data(item, 'p.styled__DarkGreyBodyText-jk5kya-0'),
            'product_link': AuxFunctions.product_link(item, 'a'),
            'product_image': AuxFunctions.product_image(item, 'img').replace(' 768w, data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw== 4000w', '')
        }
        if product_data.get('price_kg') == None:
            product = []
            product.append(product_data)
            
            SQLFunctions.insert_values(product, 'PriceTesco')
            
            
        else:
            link = product_data.get('product_link')
            product_ID = product_data.get('product_ID')
            product_image = product_data.get('product_image')
            
            ScrapeProductLink(link, product_ID, product_image)
            
            
        
        
        a+=1

        

def url(Tesco_Taxonomy):
    
    for url in Tesco_Taxonomy:
        
        aisle_url = (url.get('aisle_url'))
        #page = f'https://www.tesco.com/groceries/en-GB/shop/fresh-food/fresh-meat-and-poultry/fresh-beef'
        page = f'https://www.tesco.com/groceries/en-GB/shop{aisle_url}'
        
        driver.get(page)
        #time.sleep(3)
        ## Click to accept cookies
        click('//*[@id="sticky-bar-cookie-wrapper"]/span/div/div/div[2]/form[1]/button')
        time.sleep(3)
        soup=BeautifulSoup(driver.page_source,'lxml')
        data_page = soup.select("#product-list > div.product-list-view.has-trolley > div.pagination-component.grid > nav > ul > li")
        data_product = soup.select("#product-list > div.product-list-view.has-trolley > div.product-list-container > div > div > div.category.product-list--page.product-list--current-page > div > ul > li")
           
        #product-list > div.product-list-view.has-trolley > div.product-list-container > div > div > div.category.product-list--page.product-list--current-page > div > ul > li.styled__StyledLIProductItem-sc-198470k-1.fmKLdy.product-list--list-item.first
        #product-list > div.product-list-view.has-trolley > div.product-list-container > div > div > div.category.product-list--page.product-list--current-page > div > ul > li:nth-child(2)
        
         
        
        while next_page(data_page, soup) != None:
            
            new_link = next_page(data_page, soup)
            print(type(new_link))
            print(new_link)
            driver.get(new_link)
            time.sleep(3)
            find_data(data_product, url)
            print('==================================')
            value = find_data
            print(value)
        
            
            
            
        else:
            
            driver.get(page)
          
            find_data(data_product, url)
           
            #a+=1 
            
            #print(x)
           # print('%%%%%%%%%%%%%%%%')
        #print(data)
        #print(page)
        print('--------------------')
        ##product-list > div.product-list-view.has-trolley > div.pagination-component.grid > nav > ul > li:nth-child(3) > a
        
      ##product-list > div.product-list-view.has-trolley > div.pagination-component.grid > nav > ul > li:nth-child(6) > a
        #print(page)
        ##product-list > div.product-list-view.has-trolley > div.pagination-component.grid > nav > ul > li:nth-child(6) > a
        
        
## Run code as main

if __name__ == '__main__':                          
    url(Tesco_Taxonomy)