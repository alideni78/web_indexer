# indexing and store

# Import libs
import requests
import sqlite3
from bs4 import BeautifulSoup



# Welcome
print('''
      ################################
      #### Welcome To WEB-Indexer ####
      ################################

      ---> JUST INPUT NUMBER

        ''') 


# Input options 
def pprint ():
        print('''
        1. Look up words
        2. Exit
        ''')


# Set up Database
def db (search,x):
        conn = sqlite3.connect('indexer') 
        c = conn.cursor()
        c.execute('''
                CREATE TABLE IF NOT EXISTS word
                ([URL] TEXT ,[word_name] TEXT ,[frequency] INTEGER)
                ''')
        sql_insert = '''
                INSERT INTO word (URL, word_name, frequency)

                        VALUES
                        (?,?,?);
                '''
        data_tuple = (base_url, search, x)
        c.execute(sql_insert ,data_tuple)

        conn.commit()
        c.close()


# Set counter 
def count (search):
    counter = 0
    for i in words:
        if i == search:
            counter += 1
    return counter


# Main While

while True:
        
        # print banner
        pprint()

        # Get number
        option  = input ("> ")

        if option == "1":
                while True:
                        
                        try:
                                base_url = input("Enter URL: ")
                                r = requests.get(base_url)
                        except:
                                if requests.exceptions.MissingSchema:
                                        print("Wrong URL, Enter again")
                                        continue

                        
                        search = input ("Enter word : ")
                        
                        soup = BeautifulSoup(r.text, 'html.parser')

                        # Separate all words
                        words = soup.get_text(" ",strip=True).lower().split()

                        x = count(search)
                        db(search, x)

                        break
        
        
        elif option == "2":
                print(" Done ")
                break
