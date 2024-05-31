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
from arsenic import get_session, browsers, services


import csv



## Define OPTIONS fr the browser

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--allow-running-insecure-content')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')


#url = '/groceries/en-GB/products/250037643'
#url2 = f'https://www.tesco.com/{url}'
df = pd.read_csv("Link_List3.csv")


async def scraper(url, limit):
    
    service = services.Chromedriver(binary = r"C:\Users\nuno_\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    browser = browsers.Chrome
    browser.capabilities = {
        'goog:chromeOptions': {"args": ['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']}    
        }
    
    async with limit:
        async with get_session(service, browser) as session:
            
            
            await session.get(url)
            soup = BeautifulSoup(session.get_page_source#get_page_source,'lxml')
            something = soup.select_one('#asparagus-root > div > div.template-wrapper > main > div > div > div.styled__PDPTileContainer-mfe-pdp__sc-ebmhjv-0.cEAseF.pdp-tile > div > section.styled__GridSection-mfe-pdp__sc-ebmhjv-1.bjEIyj > h1').text
            items = {
                'url': url,
                'name': something
            }
            print(items)
     




async def run():
    
    limit = asyncio.Semaphore(10)
    
    for x in df['0']:
        url = f'https://www.tesco.com/{x}'
        
        await scraper(url, limit)
  
  
asyncio.run(run())