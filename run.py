from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials
import os
import gspread
import colorama
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_voting_system')


def display_main_menu():
    """
    Displays main menu with options to move to other areas.
    """
    cprint(figlet_format("The Voting Station!", font='big'), "green", attrs=["bold"])
    print("Welcome to the Voting Station, this is where votes are cast for the upcoming election!... \n")
    print(f"{Fore.BLUE}Please select your portal:\n")
    print("1. Voter Portal\n2. Admin Portal\n")


def select_portal():
    """
    Validates user input and directs them to selected portal.
    """
    while True:
        try:
            selection = int(input(f"{Fore.CYAN}Press 1 for Voter Portal or 2 for Admin Portal:\n"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: Please press 1 for Voter Portal or 2 for Admin Portal")
            continue
        
        if selection == 1 or selection == 2:
            break
        else: 
            print(f"{Fore.RED}Incorrect Input: Please press 1 for Voter Portal or 2 for Admin Portal")
    
    display_portal(selection)


def display_portal(portal):
    clear_terminal()
    print("Hello World")
        

def clear_terminal():
    """
    Clears the terminal.
    """
    os.system('clear')


def main():
    """
    The main function where all application functions run.
    """
    display_main_menu()
    select_portal()


main()

