## Import Libraries

import AuxFunctions
import SQLFunctions

#import pandas as pd
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException




##Define Driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



## Function to click and change options for special case products

def change_options(selector):
    try:
        return driver.find_element(By.XPATH, selector).click()
    except NoSuchElementException:
        pass



## Function for pages were options need to be choosen 

def scrape_product_page(link, product_ID, product_image):
    
    page = f'https://www.tesco.com{link}'
    print(page)
    print('______________________')
    driver.get(page)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'lxml')
    something = soup.select('#asparagus-root > div > div.template-wrapper > main > div > div > div.styled__PDPTileContainer-mfe-pdp__sc-ebmhjv-0.cEAseF.pdp-tile')

    
    if something == None:
        pass
    
    else:


        ## Function to find the diferent elements in the page
        def extract_info(selector):
            try:
                return driver.find_element(By.XPATH, selector).text
            except NoSuchElementException:
                pass


        ## Function to extract data inside product page
        def page_data(selector):
            try:
                return soup.select_one(selector).text
            except AttributeError:
                return None
        
        b = 1
        
        
        base_selector = soup.find('select', id=True)['id']  ## Used to generate XPATH for each possible selection
        selectors = [f'//*[@id="{base_selector}"]/option[1]',
                    f'//*[@id="{base_selector}"]/option[2]',
                    f'//*[@id="{base_selector}"]/option[3]',
                    f'//*[@id="{base_selector}"]/option[4]',
                    f'//*[@id="{base_selector}"]/option[5]',
                    f'//*[@id="{base_selector}"]/option[6]']
        for selector in selectors:
            change_options(selector)
            
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source,'lxml')
            
          
            product_data = {
            'extration_date': datetime.date.today(),
            'product_ID': AuxFunctions.product_code(product_ID, b),
            'product_name': str((page_data('h1.component__StyledHeading-sc-1t0ixqu-0'), extract_info(selector))).replace('("', '').replace("')", ''),
            'price': page_data('p.styled__PriceText-sc-v0qv7n-1'),
            'price_per': page_data('p.styled__Subtext-sc-v0qv7n-2'),
            'club_card_price': page_data('p.ddsweb-value-bar__content-text'),
            #'price_kg': AuxFunctions.extract_data(item, 'select'),
            'label': page_data('span.styled__StyledContainer-sc-u78h3f-0'),
            'aldi_price_label': page_data('div.styled__InfoMessageWrapper-sc-xqtzo2-0'),
            'product_link': link,
            'product_image': product_image
        }

            b+=1
           
           
           
            ## Define a stop for the loop when no more options are available
            
            stop = extract_info(selector)
            
            if stop == None:
                pass
            
            else:
                product = []
                
                product.append(product_data)
               
                
                SQLFunctions.insert_values(product, 'PriceTesco')
                
                

            
               
                


## Run code as main

if __name__ == '__main__':
    scrape_product_page(link, product_ID, product_image)