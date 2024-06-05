## IMPORT LIBRARIES


import mysql.connector





## Function to connect Python to MYSQL and save the TAXONOMY TREE data
    
def sql_save_taxonomy(table_name, tree_data):

    ## Define parametrs to connect python to MYSQL

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'YourUserName',    ##INPUT YOUR OWN USERNAME
        passwd = 'YourPasswor',    ## INPUT YOUR OWN PASSWORD
        database = 'SuperMarketScraper'
    )
    
    mycursor = db.cursor()
    

    ## Create table taxonomy


    query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, date DATE, department_name VARCHAR(50) NOT NULL, department_ID int NOT NULL, department_catId VARCHAR(100) NOT NULL, department_label VARCHAR(50) NOT NULL, category_name VARCHAR(50) NOT NULL, category_ID int NOT NULL, category_catId VARCHAR(100) NOT NULL, category_label VARCHAR(50) NOT NULL, aisle_name VARCHAR(50) NOT NULL, aisle_ID int NOT NULL, aisle_catId VARCHAR(100) NOT NULL, aisle_label VARCHAR(50) NOT NULL, aisle_allPromotionNode VARCHAR(50) NOT NULL, aisle_url VARCHAR(250) )'

    mycursor.execute(query)
    db.commit()

#def save_data( tree_data):
    ## Loop the values scraped from the webpage and insert in to the table
    for value in tree_data:
        #x = value.get('shleve_ID')

        #query = "INSERT IGNORE INTO " + table_name + " (ID, department, category, aisle, shelve, web_page_ID) VALUES ( %(shleve_ID)s, %(department_name)s, %(category_name)s, %(aisle_name)s, %(shelve)s, %(web_ID)s), value)

        mycursor.execute("INSERT IGNORE INTO " + table_name + " (date, department_name, department_ID, department_catId, department_label, category_name, category_ID, category_catId, category_label, aisle_name, aisle_ID, aisle_catId, aisle_label, aisle_allPromotionNode, aisle_url) VALUES (%(date)s, %(department_name)s, %(department_ID)s, %(department_catId)s, %(department_label)s, %(category_name)s, %(category_ID)s, %(category_catId)s, %(category_label)s,%(aisle_name)s,%(aisle_ID)s, %(aisle_catId)s, %(aisle_label)s,%(aisle_allPromotionNode)s, %(aisle_url)s)", value)
    db.commit()
    
    
    
    
    
    
## Function to create and insert data into table

def insert_values(page_data, table_name):

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'YourUserName',    ##INPUT YOUR OWN USERNAME
        passwd = 'YourPasswor',    ## INPUT YOUR OWN PASSWORD
        database = 'SuperMarketScraper'
    )


    mycursor = db.cursor()

    query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID INT AUTO_INCREMENT primary key NOT NULL, Date DATE, product_ID int, Product VARCHAR(250), Product_Link VARCHAR(250), Price VARCHAR(50), Price_Per VARCHAR(50), club_card_price VARCHAR(50), Label VARCHAR(250), aldi_price_label VARCHAR(50), product_image VARCHAR(250))'

    mycursor.execute(query)
    db.commit()

    mycursor = db.cursor()

    for value in page_data:
    
        mycursor.execute("INSERT IGNORE INTO " + table_name + " (Date, product_ID, Product, Product_Link, Price, Price_Per, club_card_price, Label, aldi_price_label, product_image) VALUES ( %(extration_date)s, %(product_ID)s, %(product_name)s, %(product_link)s, %(price)s, %(price_per)s, %(club_card_price)s,  %(label)s,  %(aldi_price_label)s,  %(product_image)s)", value)
        

        db.commit()
