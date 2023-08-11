"""
Main file to run the application. 
"""

"""
Import libraries/ packages. 
"""
import os
import sys
import random
import pyinputplus as pyip
from tabulate import tabulate
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
TODO: Delete coded out comment
"""

#main_list = SHEET.worksheet('main_list')

#complete_list = main_list.get_all_values()

#print(complete_list)

"""
Global variables for app processes.
"""

"""
Variables for sheet in the spreadsheet.
TODO: Rewrite use correct gpsread terminology
"""
LIST_ALL = SHEET.worksheet('main_list')


def welcome_message():
    """
    Application introduction that explains the purpose of the application 
        and gives instructions to the user. 
    TODO: Rewrite comment to avoid plagiarism. 
    """
    clear_tmnl
    print("Welcome to the Children's Book Picker\n")
    print("Please select an option below.\n")
    """TODO: Rewrite instruction to avoid plagiarism. """
    print(colored(("(1) List all books"), "green"))
    print(colored(("(2) Early Childhood 0-5 year olds"), "green"))
    print(colored(("(3) Middle Childhood 6-8 year olds"), "green"))
    print(colored(("(4) Late Childhood 9-11 year olds"), "green"))
    print(colored(("(5) Adolescence 12-14 year olds"), "green"))
    print(colored(("(6) Search for a book"), "green"))
    
    while True:
        welcome_message_ans = input ("\n")
        if welcome_message_ans not in ("1", "2", "3", "4", "5"):
            print ("Invalid input. Please try again.")
            print ("Please choose an option between 1 and 5.")
        else:
            break
        
    if welcome_message_ans == ("1"):
         main_list ()
    #elif welcome_message_ans == ("2"):
        #early_childhood ()
    #elif welcome_message_ans == ("3"):
        #middle_childhood ()
    #elif welcome_message_ans == ("4"):
        #late_childhood ()
    #elif welcome_message_ans == ("5"):
        #adolescence ()
    #elif welcome_message_ans == ("6"):
       #search_book ()
        
def main_list ():
    """
    List all books in the spreadsheet. 
    """
    clear_tmnl()
    all_books = SHEET.worksheet('main_list') #FIXME: Can I keep the name or must it be change to main_list?
    all_rows = []
    for ind in range(1,22): #FIXME: Found out if 22 is the correct number in the spread sheet. 
        all_col = all_books.col_values(ind) #FIXME: ind column name or Python tech?
        all_rows.append(all_col[1: ])
    title = all_rows[0]
    author = all_rows[1]
    illustrator = all_rows[2]
    interest_level = all_rows[3]
    reading_age = all_rows[4]
    synopsis = all_rows[5]
    
    print('\n Complete Book List:\n')
    #FIXME: Code snippet
    all_books = SHEET.worksheet('main_list') #FIXME: Can I keep the name or must it be change to main_list?
    all_rows = []
    for ind in range(1,22): #FIXME: Found out if 22 is the correct number in the spread sheet. 
        all_col = all_books.col_values(ind) #FIXME: ind column name or Python tech?
        all_rows.append(all_col[1: ])
    title = all_rows[0]
    author = all_rows[1]
    illustrator = all_rows[2]
    interest_level = all_rows[3]
    reading_age = all_rows[4]
    synopsis = all_rows[5]
    
    print('\n Complete Book List:\n')
    #FIXME: Code snippet
    #for (title, author, illustrator, interest_level, reading_age, synopsis) in zip (title, author, illustrator, interest_level, reading_age, synopsis):
       #print(f' {title} by {author} by {illustrator} with {interest_level} interest)
             
    print('\n Synopsis:\n')
    for synopsis in synopsis:
        print(synopsis)
        
        print(colored(("(0) Return to main menu"), "green"))
    
    while True:
        main_list_ans = input ("\n")
        if main_list_ans not in ("0"):
            print(colored(("Invalid input. Please try again."), "red"))
            print(colored(("Please choose 0 to return to the main menu."), "red"))
        else:
            break
        
    if main_list_ans == ("0"):
        welcome_message()


     
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
    