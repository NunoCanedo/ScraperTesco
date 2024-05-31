from concurrent.futures import ThreadPoolExecutor
import csv
import time
from multiprocessing import Pool
import multiprocessing

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_links():
    links = []
    with open('Link_list3.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            links.append(row[0])
            
        return links
    
def data(url):
    driver.get(f'https://www.tesco.com/{url}')
        #time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'lxml')
    try:
        something = soup.select_one('#asparagus-root > div > div.template-wrapper > main > div > div > div.styled__PDPTileContainer-mfe-pdp__sc-ebmhjv-0.cEAseF.pdp-tile > div > section.styled__GridSection-mfe-pdp__sc-ebmhjv-1.bjEIyj > h1').text
        items = {
            'url': url,
            'name': something
        }
            
        print(items)
    except AttributeError:
        pass
    
       
def scraper():
    
    start_time = time.time()
    
    url = get_links()
    
    with ThreadPoolExecutor(max_workers=100) as p:
        results = p.map(data, url)
        for result in results:
            print(result)
    
       
        
        
    print(f'{(time.time() - start_time):.2f} secondes')
    
scraper()