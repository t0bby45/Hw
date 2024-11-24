import sqlite3
from bs4 import BeautifulSoup
import requests

while(True):
    print("1. Add website")
    print("2. Find Keyword")
    print("3. Delete Website")
    print("4. Exit Website")
    command = int(input())
    if(command == 1):
        print("Please input the name of website with https")
        url = input()
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute("Create table if not exists website(name text)")
        cur.execute("insert into website(name) values (?)", (url,))
        connection.commit()
        connection.close()
        print("success!")

    elif(command == 2):
        print("Please input the name of website with https")
        url = input()
        print("Please input the keyword from website")
        key = input()
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute('select * from website where name = ?', (url,))
        row = cur.fetchall()
        if row:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            keyword_count = text.lower().count(key.lower())
            print("Found " + str(keyword_count) + " keywords.")
        else:
            print("No such website is in the Database")
        connection.commit()
        connection.close()

    elif(command == 3):
        print("Please input the name of website with https")
        url = input()
        connection = sqlite3.connect('main.sl3')
        cur = connection.cursor()
        cur.execute('select * from website where name = ?', (url,))
        row = cur.fetchall()
        if row:
            cur.execute('delete from website where name = ?', (url,))
            print("Deleted!")
        else:
            print("No such website is in the Database")
        connection.commit()
        connection.close()
    else:
        print("Goodbye!")
        break


