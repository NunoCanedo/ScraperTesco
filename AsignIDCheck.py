## Import Libraries


import pandas as pd
from csv import reader
import concurrent.futures
import asyncio
import csv

from concurrent.futures.thread import ThreadPoolExecutor


import time
import datetime
#import mysql.connector

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options



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


Tesco_Taxonomy = csv.DictReader(open("Tesco_Taxonomy.csv"))


executor = ThreadPoolExecutor(10)


def scrape(url, *, loop):
    loop.run_in_executor(executor, scraper, url)
    
def scraper(url):
    link_list = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f'https://www.tesco.com/{url}')
    driver.get_screenshot_as_file("screenshot.png")



loop = asyncio.get_event_loop()
for url in Tesco_Taxonomy:
    aisle_url = (url.get('aisle_url'))
    scrape(aisle_url, loop=loop)
    

loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop)))


