"""
Garrett May
12 May 2022
CSD310-306J Database Development and Use
Module 12: WhatABook
"""

""" import statements """
import sys
import csv
import mysql.connector
from mysql.connector import errorcode

""" database config object """    
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# main method 
def main():
    menu()
   
# main menu   
def menu():
    
    print("\n ----- Welcome to WhatABook -----")
    print()
    
    print("""       Please choose and option below.
          
                    1. View Books
                    2. View Store Location
                    3. View Account
                    4. Exit""")
    
    while True: 
        try: 
            choice = (int(input("""
                                Enter in the number associated with your choice:
                                Example: 1 would bring you to the View Books: """)))
            
            if choice == 1: 
                view_books()
                break
            elif choice == 2:
                view_store_location()
                break
            elif choice == 3: 
                my_account()
                break
            elif choice == 4:
                print("\n ----- Thank you, come again! -----")
                break
            else: 
                print("Please only select a number 1 - 4.")
                print("Please try again")
            
        except ValueError:
            print(" Invalid Selection. Please only select a number 1 - 4")
            
            
# display books
def view_books():
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    
    books = cursor.fetchall()
    
    print("\n ----- Display book listings -----")
    
    for book in books: 
        print("\nBook ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Details: {}".format(book[2]))
        print("Details: {}".format(book[3])) 
        

    
def view_store_location():
    
    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()
    cursor.execute("SELECT store_id, local FROM store")
    
    locations = cursor.fetchall()
    
    print("\n ----- Displaying Store Location -----\n")
    
    for location in locations: 
        print(" Local: {}".format(location[1]))
        break
    
    
    
# verify user
def my_account():
        
    while True:
        try:
            global user_id 
            user_id = (int(input(""" We need to verify your identity!
                                     Enter your customer ID: """))) 
                
            if user_id >= 1 and user_id <= 3:
                show_account_menu()
                break
                
            else:
                print("\n ----- Invalid Customer ID -----") 
                print("\n ----- Please try again -----")
                my_account()
                
        except ValueError:
            print("\n ----- Invalid Selection. Enter a valid user ID. -----") 
            my_account()
        my_account() 
            
# display user menu
def show_account_menu():
    
    print("\n ----- Welcome to your WhatABook Account -----")
    print() 
    
    print("\n ----- Customer Menu -----")
    print(""" Please make a Selection.
          
                1. Show wishlist
                2. Show books
                3. Add books to wishlist
                4. Main menu
                5. Exit Program """)
    
    while True:
        try:
            
            account_choice = (int(input("""
                                        
            Enter in the number associated with your choice:
            Example: 1 would bring you to the Show wishlist. """)))
            
            if account_choice == 1: 
                show_wishlist()
                break
            elif account_choice == 2:
                view_books()
                break
            elif account_choice == 3:  
                view_books()
                add_book_to_wishlist()
                break
            elif account_choice == 4:
                
                break
            elif account_choice ==5:
                print("\n ----- Thank you, come again! -----") 
                
                break
            else: 
                print(" Please only select a number 1 - 5")
                print(" Please try again.")
            show_account_menu()
        except ValueError:
            print(" Invalid Choice. Enter a number 1 - 5")
            show_account_menu
    show_account_menu()
    
# display user wishlist
def show_wishlist(user_id):
    
    db = mysql.connector.connect(**config) 
    
    cursor = db.cursor()
    
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
                   "FROM wishlist " + 
                   "INNER JOIN user ON wishlist.user_id = user.user_id " +
                   "INNER JOIN book ON wishlist.book_id = book.book_id " +
                   "WHERE user.user_id = {}".format(user_id)) 
    
    wishlist = cursor.fetchall()
    
    print("\n ----- Displaying Wishlist -----") 
    
    for book in wishlist:
        print("\nBook Name: {}".format(book[4])) 
        print("Author: {}".format(book[5]))
        print() 
        
    show_account_menu()
    
# display books to add
def show_books_to_add(user_id):
    
    db = mysql.connector.connect(**config) 
    
    cursor = db.cursor() 
    
    # query books
    query = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist user_id = {}".format(user_id))

    print(query) 
    
    cursor.execute(query) 
    
    books_to_add = cursor.fetchall() 
    
    print("\n ----- Displaying Available Books -----") 
    
    for book in books_to_add:
        print("\nBook ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Book Author: {}".format(book[2]))
        print("Book Details: {}".format(book[3]))
        print() 
        
# add books to wishlist
def add_book_to_wishlist(book_id, user_id):
    
    
    try:
            
        db = mysql.connector.connect(**config) 
            
        cursor = db.cursor()
        book_id = int(input("\nEnter the id of the book you would like to add: "))
            
        if book_id >= 1 and book_id <= 9: 
            cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id)) 
            db.commit()
            show_account_menu() 
            
        else: 
            print("\n Invalid Selection. Enter 1 - 9")
                
    except ValueError:
        print("\nInvalid Selection. Enter 1 - 9")
        add_book_to_wishlist()
            
                                                                         
           

