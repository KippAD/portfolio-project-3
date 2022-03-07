import os
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials
import strings
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
    print(strings.main_menu_text)


def select_portal():
    """
    Validates user input and directs them to selected portal.
    """
    chosen_portal = validate_menu_selection("Voter Portal", "Admin Portal")
    reset_terminal()

    if chosen_portal == 1:
        load_voter_portal()
    else:
        load_admin_portal()


def load_voter_portal():
    """
    Loads voter portal menu displays possible options for user
    to select next.
    """
    print(strings.voter_portal_text)
    voter_menu = validate_menu_selection("Cast Vote", "View Result")

    if voter_menu == 1:
        print("Loading the voting station...\n")
        cast_user_vote()
    else:
        print("Loading voting results...\n")


def load_admin_portal():
    """
    Loads admin men if login is correctly input by the user. 
    Displays options to view vote results and voting insights.
    """
    validate_admin_login()
    print(strings.admin_portal_text)
    admin_menu = validate_menu_selection("Vote Results", "Voting Insights")

    if admin_menu == 1:
        print("Loading results...")
    else:
        print("Loading insights...")


def cast_user_vote():
    """
    Takes validated user inputs to build list that is
    will be submitted as a vote to the external google spreadsheet.
    """
    reset_terminal()
    print(f"{Fore.MAGENTA}Welcome to the Voting Station!\n")
    print(f"{Fore.CYAN}In order to cast your vote, please fill out the form below\n")

    name_input = get_voter_name()
    age_input = get_voter_age()


def get_voter_name():
    """
    Concatenates the two strings passed through the validate_vote_name 
    function and returns them as a single string.
    """
    fname = validate_vote_name("first")
    lname = validate_vote_name("last")
    full_name = fname + " " + lname

    return full_name


def validate_vote_name(name_type):
    """
    Ensures that data submitted when user cast votes is correct
    before data is submitted to spreadsheet.
    """
    while True:
        try:
            name = str(input(f"{Fore.CYAN}Please enter your {name_type} name:\n"))
            name = name.title()
        except ValueError:
            print(f"{Fore.RED}\nYour name can only contain letters.\n")
            print(f"{Fore.CYAN}Please exclude any numbers, spaces, or characters...")
            continue

        if name.isalpha():
            break
        else:
            print(f"{Fore.RED}\nYour name can only contain letters.\n")
            print(f"{Fore.RED}Please exclude any numbers, spaces, or characters...\n")

    return name


def get_voter_age():
    """
    Gets voters age from an input, validates that the value is
    an integer between 18 and 120 and returns the value.
    """
    while True:
        try:
            age = int(input(f"{Fore.CYAN}Please enter your age:\n"))
        except ValueError:
            print(f"{Fore.RED}You age can only contain numbers!\n")
            continue
        else:
            if age >= 18 and age <= 120:
                print(f"{Fore.GREEN}Age entered...")
                break
            else:
                print(f"{Fore.RED}Please enter an age between 18 and 120:\n")
    
    return age

def validate_menu_selection(choice1, choice2):
    """
    Ensures that the correct input is given by the user in
    the multiple choice menu that appears throughout the
    application.
    """
    while True:
        try:
            selection = int(input(f"{Fore.CYAN}Press 1 for {choice1} or 2 for {choice2}:\n"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: Please press 1 for {choice1} or 2 for {choice2}\n")
            continue

        if selection == 1 or selection == 2:
            break
        else:
            print(f"{Fore.RED}Incorrect Input: Please press 1 for {choice1} or 2 for {choice2}\n")

    return selection


def validate_admin_login():
    """
    Asks the user to enter the admin and password required to access
    the admin portal and ensures that the login details are correct
    before allowing access.
    """
    print(f"{Fore.CYAN}Welcome Admin! Please login in to access the admin portal.\n")
    username = "admin"
    password = "password"

    while True:
        username_attempt = input(f"{Fore.CYAN}Please enter the username:\n")
        password_attempt = input(f"{Fore.CYAN}Please enter the password:\n")

        if username_attempt == username and password_attempt == password:
            print(f"{Fore.GREEN}Login detail correct")
            print(f"{Fore.MAGENTA}Loading Admin Portal...")
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
