## Import Libraries

from bs4 import BeautifulSoup



## Function to join the page ID with the product ID to generate a unique product ID
  
def product_code(num1, num2):
  return int("{}{}".format(num1, num2))




## Function to TRY and Extract the individual data from each product in the Page being scraped
        
def extract_data(product, selector):
  try:
    return product.select_one(selector).text
  except AttributeError:
    return None
  
  

## Function for the Product Link 
  
def product_link(item, selector):
    
    try:
        return item.find(selector, href=True)['href']
    
    except TypeError:
        return None
      
      
## Function for the Product Image 
  
def product_image(item, selector):
    
    try:
        return item.find(selector, srcset=True)['srcset']
    
    except TypeError:
        return None