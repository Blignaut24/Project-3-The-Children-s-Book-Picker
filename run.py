"""
Main file to run the application. 
"""

"""
Import libraries/ packages. 
"""
import os
import sys
import random
from termcolor import colored
import gspread
from google.oauth2.service_account import Credentials
 

# The scope was inspired by and borrowed from
# Code Instituet Love Sandwiches project
# https://github.com/Code-Institute-Solutions/love-sandwiches-p4-sourcecode
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('book_list')

"""
Global variables for app processes.
"""

"""
Variables for sheet in the worksheet.
"""
LIST_ALL = SHEET.worksheet('main_list')


def welcome_message():
    """
    A welcome message that provides the main menu of the application.
    """
    clear_tmnl()
    print("Welcome to the Children's Book Picker\n")
    print("Please select an option below.\n")
    print(colored(("(1) List all books"), "green"))
    print(colored(("(2) Random Book Picker"), "green"))
    print(colored(("(3) Search"), "green"))
    
    while True:
        welcome_message_ans = input ("\n")
        if welcome_message_ans not in ("1", "2", "3"):
            print ("Invalid input. Please try again.")
            print ("Please choose an option between 1 and 3.")
        else:
            break
        
    if welcome_message_ans == ("1"):
         load_books ()
    elif welcome_message_ans == ("2"):
        random_book_picker()
    #elif welcome_message_ans == ("3"):
        #Search ()
        
def load_books():
    """
    List all books in the spreadsheet. 
    """
    clear_tmnl()
    all_books = SHEET.worksheet('main_list') 
    headerSpreadsheet = all_books.row_values(1)
    numberOfBooks = len(all_books.col_values(1))-1
    numberOfColumns = len(all_books.row_values(1))
       
    all_rows = []
    for ind in range(1,22):
        all_col = all_books.col_values(ind) 
        all_rows.append(all_col[1: ])
    title = all_rows[0]
    author = all_rows[1]
   
    # TODO: author =  all_books.col_values(2)     #HK: alternative way to get author, first take all column including header(row1)
    # TODO: author = author[1:]                   #HK: remove row 1 (since it is already in python, we start counting at 0, so we omit 0 and start at 1)
  
    illustrator = all_rows[2]
    interest_level = all_rows[3]
    reading_age = all_rows[4]
    reading_stage = all_rows[5]
    synopsis = all_rows[6]
    
 
    # TODO: for row in all_books:
        # TODO: print(row[0])
      
    print('\n Complete Book List:\n')            
    print('\n Book Titles:\n')
    for ind in range(numberOfBooks):
        print(f"{title[ind]} - {author[ind]}")
        
    print(colored(("(0) Return to main menu"), "green"))
    
    while True:
        main_list_ans = input ("\n")
        if main_list_ans not in ("0"):
            print(colored(("Invalid input. Please try again."), "red"))
        else:
            break
        print(colored(("Please choose 0 to return to the main menu."), "red"))

        
    if main_list_ans == ("0"):
        welcome_message()
        
def random_book_picker():
    """
    This feature helps users randomly select a book from the following categories: 
    early childhood, middle childhood, late childhood, and adolescence.
    """
    clear_tmnl()
    print("The Random Book Picker chooses a book at random from the selected category, \n")
    print ("taking into account the child's expected mental and developmental age. \n")
    print("Please select a category:\n")
    print(colored(("(1) Early Childhood 0-5 years old"), "green"))
    print(colored(("(2) Middle Childhood 6-8 years old"), "green"))
    print(colored(("(3) Late Childhood 9-11 years old"), "green"))
    print(colored(("(4) Adolescence 12-15 years old"), "green"))
  
    

    print(colored(("(0) Return to main menu"), "green"))
    
    while True:
        main_list_ans = input ("\n")
        if main_list_ans not in ("0"):
            print(colored(("Invalid input. Please try again."), "red"))
        else:
            break
        print(colored(("Please choose 0 to return to the main menu."), "red"))

        
    if main_list_ans == ("0"):
        welcome_message()  
    
    

# def search():



     
def clear_tmnl():
    """
    Clears the terminal when called.
    TODO: Write credit into my README.md from doctor-dairy project.
    """
    # Idea taken from a post on slack.
    # (Credited in readme)
    os.system("clear")

            
def main ():
    """
    Runs necessary functions at the start of the program
    """
    welcome_message()
    
 
main()
    