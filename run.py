import os
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials
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
    reset_terminal()
    print("Welcome to the Voting Station!")
    print("Cast your vote for the upcoming election!... \n")
    print(f"{Fore.BLUE}Please select your portal:\n")
    print("1. Voter Portal\n2. Admin Portal\n")


def select_portal():
    """
    Validates user input and directs them to selected portal.
    """
    chosen_portal = validate_menu_selection("Voter Portal", "Admin Portal")

    if chosen_portal == 1:
        load_voter_portal()
    else:
        load_admin_portal()


def load_voter_portal():
    """
    Loads voter portal menu if chosen by user.
    """
    reset_terminal()
    print("You have chosen the voter portal")


def load_admin_portal():
    """
    Loads admin men if login is correctly input by the user. 
    Displays options to view vote results and voting insights.
    """
    reset_terminal()
    print(f"{Fore.CYAN}Welcome Admin! Please login in to access the admin portal.\n")
    validate_admin_login()

    print(f"{Fore.BLUE}Welcome to the Admin Portal!\n")
    print("1. Vote Results\n2. Voting Insights\n")

    admin_menu = validate_menu_selection("Vote Results", "Voting Insights")
    
    if admin_menu == 1:
        print("Loading results...")
    else:
        print("Loading insights...")


def validate_menu_selection(choice1, choice2):
    """
    Ensures that the correct input is given by the user in 
    multiple choice menu (main menu and admin menu).
    """
    while True:
        try:
            selection = int(input(f"{Fore.CYAN}Press 1 for {choice1} or 2 for {choice2}:\n"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: Please press 1 for {choice1} or 2 for {choice2}")
            continue

        if selection == 1 or selection == 2:
            break
        else:
            print(f"{Fore.RED}Incorrect Input: Please press 1 for {choice1} or 2 for {choice2}")
 
    return selection


def validate_admin_login():
    """
    Validates the username and password entered by the user
    in order to access the admin portal.
    """
    username = "admin"
    password = "password"

    while True:
        username_attempt = input(f"{Fore.BLUE}Please enter the username:\n")
        password_attempt = input(f"{Fore.BLUE}Please enter the password:\n")

        if username_attempt == username and password_attempt == password:
            print(f"{Fore.GREEN}Login detail correct")
            print(f"{Fore.CYAN}Loading Admin Portal...")
            break
        else:
            print(f"{Fore.RED}Incorrect login")
    
    reset_terminal()


def reset_terminal():
    """
    Clears the terminal.
    """
    os.system('clear')
    cprint(figlet_format("The Voting Station!", font='big'), "green", attrs=["bold"])


def main():
    """
    The main function where all application functions run.
    """
    display_main_menu()
    select_portal()


main()
