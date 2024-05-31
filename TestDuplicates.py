import re


rest_shelve = '/groceries/en-GB/shop/fresh-food/fresh-meat-and-poultry/burgers-meatballs-and-bbq-meat/bbq-chicken'
taxonomy_url = '/fresh-food/fresh-meat-and-poultry/burgers-meatballs-and-bbq-meat'
url_fix = rest_shelve.replace('/groceries/en-GB/shop', '')

#print(rest_shelve)
#print(taxonomy_url)
#print(url_fix)

x = re.split('/', rest_shelve)
#print(x[7])
final_url = url_fix.replace(str(x[7]), '')
final = final_url.replace('/', '')
#print(final)


#target = re.sub('\s',rest_shelve)
#print(target)
test = re.findall('/[\w\-]+',rest_shelve)
#print(test[6])
test_final = url_fix.replace(str(test[6]), '')
print(rest_shelve)
print(test_final)
print(taxonomy_url)

import pandas as pd
data = pd.read_pickle("ingr_map.pkl")
print(data)