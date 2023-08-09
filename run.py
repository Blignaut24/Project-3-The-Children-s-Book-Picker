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
    print("Welcome to the Children's Book Picker\n")
    print("Please select an option below.\n")
    """TODO: Rewrite instruction to avoid plagiarism. """
    
    print(colored(("(1) List all books"), "green"))
    print(colored(("(2) Early Childhood 0-5 year olds"), "green"))
    print(colored(("(3) Middle Childhood 6-8 year olds"), "green"))
    print(colored(("(4) Late Childhood 9-11 year olds"), "green"))
    print(colored(("(5) Adolescence 12-14 year olds"), "green"))
    
    while True:
        welcome_message_ans = input ("\n")
        if welcome_message_ans not in ("1", "2", "3", "4", "5"):
            print ("Invalid input. Please try again.")
            print ("Please choose an option between 1 and 5.")
        else:
            break
        
    if welcome_message_ans == ("1"):
         main_list ()
    elif welcome_message_ans == ("2"):
        early_childhood ()
    #elif welcome_message_ans == ("3"):
        #middle_childhood ()
    #elif welcome_message_ans == ("4"):
        #late_childhood ()
    #elif welcome_message_ans == ("5"):
        #adolescence ()
        
def main_list ():
    """
    List all books in the spreadsheet. 
    """
    main_list = SHEET.worksheet('main_list')

    complete_list = main_list.get_all_values()
    
    print(complete_list)
    
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
            
def main ():
    """
    Runs necessary functions at the start of the program
    """
    welcome_message()
    
 
main()
    