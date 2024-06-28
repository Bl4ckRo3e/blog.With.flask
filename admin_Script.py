import sqlite3
from pyfiglet import Figlet
import terminal_banner
import os
import time


class Add:
    def add_cat(this, name, id):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            data = (id, name)
            # Insert data into table
            cursor.execute('INSERT INTO Categories (id,name) VALUES (?, ?)', data)
            # Commit changes and close connection
            conn.commit()
            conn.close()
            print("Added")
        except:
            print("Not Add")
        

    def add_user(this, name, mode, email, code, id):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            data = (id, name, email,code, mode)
            # Insert data into table
            cursor.execute('INSERT INTO Users (id,name,email,code,mode) VALUES (?, ?, ?, ?, ?)', data)
            # Commit changes and close connection
            conn.commit()
            conn.close()
            print("Added")
        except:
            print("Not Add")

    def add_article(this, id, title, content, image, cat, user_mode, active, count, writer):
        # try:
        #     # Read the image file
        #     # with open(image, 'rb') as file:
        #     #     image_data = file.read()
        #     # Connect to SQLite database
        #     conn = sqlite3.connect('Database.db')
        #     cursor = conn.cursor()
        #     data = (id, title, content, image, cat,user_mode, active, count, writer)
        #     # Insert data into table
        #     cursor.execute('INSERT INTO Articles (id, title, content, image_data, category, user_mode, active, writer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
        #     # Commit changes and close connection
        #     conn.commit()
        #     conn.close()
        #     print("Added")
        # except:
        #     print("Not Add")
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            data = (id, title, content, image, cat,user_mode, active, count, writer)
            # Insert data into table
            cursor.execute('INSERT INTO Articles (id, title, content, image_data, category, user_mode, active, count, writer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
            # Commit changes and close connection
            conn.commit()
            conn.close()
            print("Added") 
    
    def main(this):
        # this is for Greating
        custom_fig = Figlet(font='graffiti')
        print(custom_fig.renderText('Hello and Welcome !'))
        # this is for about 
        banner_text = "[+] Add To database :\n[1] Add Category\n[2] Add User\n[3] Add Article\n\n[4] Exit.\n[&] Clear"
        my_banner = terminal_banner.Banner(banner_text)
        print(my_banner)


if __name__ in '__main__':
    Adder = Add()
    while True:
        os.system('clear')
        Adder.main()
        user_input = int(input("> "))
        if user_input == 4:
            print("Good Bye")
            break
        elif user_input == 1:
            os.system('clear')
            # this is for about 
            banner_text = "Add Category\nOnly Enter Name of Category"
            my_banner = terminal_banner.Banner(banner_text)
            print(my_banner)
            id_cat   = int(input('id>'))
            name_cat = input('name> ')
            Adder.add_cat(name_cat, id_cat)
            time.sleep(2)
        elif user_input == 2:
            os.system('clear')
            # this is for about 
            banner_text = "Add User\nEnter all parameters in here"
            my_banner = terminal_banner.Banner(banner_text)
            print(my_banner)
            id_user = int(input('id> '))
            name    = input("name> ")
            email   = input('email> ')
            code    = int(input('code> '))
            mode    = input('mode> ')
            Adder.add_user(name,mode, email,code,id_user)
            time.sleep(2)
        elif user_input == 3:
            os.system('clear')
            # this is for about 
            banner_text = "Add Article\nEnter all parameters in here"
            my_banner = terminal_banner.Banner(banner_text)
            print(my_banner)
            count = 0
            id_user = int(input('id> '))
            name    = input("title> ")
            conte   = input('content> ')
            image   = (input('image path> '))
            cate    = input('category> ')
            user    = input('user mode> ')
            active  = input("Status>")
            writer  = input('writer name>')
            Adder.add_article(id_user, name, conte, image, cate, user, active, count, writer)
            time.sleep(2)
        else:
            os.system('clear')
