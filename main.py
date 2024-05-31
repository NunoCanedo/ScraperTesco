import requests



url = 'https://www.tesco.com/groceries/en-GB/taxonomy'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
data = requests.get(url,headers=headers).json()




def category(items):
    
    for category in items.get('department_children'):
        
        
        
        category = {
            'department_name': items.get('name')
        }
        
    
        
        #print(category)
        #print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')






def parser(url, headers):
    
    tree = requests.get(url, headers=headers).json()
    
    a = 10
    
    for department in tree:

        department = {
            'department_name': department.get('name'),
            'department_ID': a,
            'department_catId': department.get('catId'),
            
            'department_label': department.get('label'),
            'department_children': department.get('children'),
            
            
        }
        
        a+=1
        
        print(department)
        print('##################')
       
        
        category(department)
        
    
    
parser(url, headers)