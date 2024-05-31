from concurrent.futures import ThreadPoolExecutor
import csv
import time
import asyncio
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import asyncio


import csv



## Define OPTIONS fr the browser

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--allow-running-insecure-content')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')




def scraper(url):
    link_list = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    try:
        soup = BeautifulSoup(driver.page_source,'lxml')
        something = soup.select_one('#asparagus-root > div > div.template-wrapper > main > div > div > div.styled__PDPTileContainer-mfe-pdp__sc-ebmhjv-0.cEAseF.pdp-tile > div > section.styled__GridSection-mfe-pdp__sc-ebmhjv-1.bjEIyj > h1').text
        items = {
            'url': url,
            'name': something
        }
        
        link_list.append(items)
        link_list_csv = pd.DataFrame(link_list)
        link_list_csv.to_csv('Link_List4.csv', mode='a', index=False, header=False)
        driver.quit()
    except AttributeError:
        return None
    
    
    

def run():
   
        
    df = pd.read_csv("Link_List3.csv")
    for url in df['0']:
   
        url = f'https://www.tesco.com{url}'
        scraper(url)
        
        
        
        

if __name__ == '__main__':
    start = time.time()
    run()
    end = time.time() - start
    print(f'total time is: {end}')