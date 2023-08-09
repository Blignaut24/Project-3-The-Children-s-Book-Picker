"""
Main file to run the application. 
"""

"""
Import libraries/ packages. 
"""
import os
import sys
import pyinputplus as pyipfrom tabulate import tabulate
from tabulate import tabulate
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

main_list = SHEET.worksheet('main_list')

complete_list = main_list.get_all_values()

print(complete_list)