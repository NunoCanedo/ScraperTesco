## IMPORT LIBRARIES


import requests
import AuxFunctions
import SQLFunctions
import datetime
import PageScraper
import pandas as pd



url = 'https://www.tesco.com/groceries/en-GB/taxonomy'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
data = requests.get(url,headers=headers).json()

taxonomy = []

## First function to find and AISLES and give a value for ID

def aisle(category_children, category_data):
    
    c = 10
    
    if category_children != None:
        
        for aisle in category_children:
            aisle_data = {
                'date': datetime.date.today(),
                'department_name': category_data.get('department_name'),
                'department_ID': category_data.get('department_ID'),
                'department_catId': category_data.get('department_catId'),
                'department_label': category_data.get('department_label'),
                'category_name': category_data.get('category_name'),
                'category_ID': category_data.get('category_ID'),
                'category_catId': category_data.get('category_catId'),
                'category_label': category_data.get('category_label'),
                'aisle_name': aisle.get('name'),
                'aisle_ID': AuxFunctions.product_code(category_data.get('category_ID'), c),
                'aisle_catId': aisle.get('catId'),
                'aisle_label': aisle.get('label'),
                'aisle_allPromotionNode': aisle.get('allPromotionNode'),
                'aisle_url': aisle.get('url')         
            }
            
            Tesco_Taxonomy = []
            Tesco_Taxonomy.append(aisle_data)
            
            SQLFunctions.sql_save_taxonomy('TescoTaxonomy2', Tesco_Taxonomy)
            #print('**********************************')
            #print(aisle)
            #print('>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        
            c+=1
            taxonomy.append(aisle_data)
            df = pd.DataFrame(taxonomy)
            df.to_csv('Tesco_Taxonomy.csv', index=False)
           
    
    
    
        
## First function to find and CATEGORIES and give a value for ID

def category(department_children, department_data):
    
    b = 10
    
    for category in department_children:
        #print(x)
        category_children = category.get('children')
        category_data = {
            
                'department_name': department_data.get('department_name'),
                'department_ID': department_data.get('department_ID'),  ## Asign a value for ID
                'department_catId': department_data.get('department_catId'),
                'department_label': department_data.get('department_label'),
                'category_name': category.get('name'),
                'category_ID': AuxFunctions.product_code(department_data.get('department_ID'), b),
                'category_catId': category.get('catId'),
                'category_label': category.get('label')
                
                
        }
        #print(category_data)
        #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        b+=1
        aisle(category_children, category_data)
    
    

## First function to find and DEPARTMENTS and give a value for ID

def department(data):

    a = 10

    for department in data:
            
            
            department_children = department.get('children')
            department_data = {
                'department_name': department.get('name'),
                'department_ID': a,  ## Asign a value for ID
                'department_catId': department.get('catId'),
                'department_label': department.get('label'),
                'department_children': department.get('children')
                
            }
          
            
            a+=1
            
            category(department_children, department_data)



## Run code as main

if __name__ == '__main__':                          
    department(data)       