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
    chosen_portal = validate_menu_selection("Voter Portal", "Admin Portal", "Information")
    reset_terminal()

    if chosen_portal == 1:
        load_voter_portal()
    elif chosen_portal == 2:
        load_admin_portal()
    else:
        load_information()


def load_voter_portal():
    """
    Loads voter portal menu displays possible options for user
    to select next.
    """
    reset_terminal()
    print(strings.voter_portal_text)
    voter_menu = validate_menu_selection("Cast Vote", "View Result", "Main Menu")

    if voter_menu == 1:
        print("Loading the voting station...\n")
        cast_user_vote()
    elif voter_menu == 2:
        print("Loading voting results...\n")
    else:
        main()


def load_admin_portal():
    """
    Loads admin men if login is correctly input by the user. 
    Displays options to view vote results and voting insights.
    """
    validate_admin_login()
    print(strings.admin_portal_text)
    admin_menu = validate_menu_selection("Vote Results", "Voting Insights", "Main Menu")

    if admin_menu == 1:
        print("Loading results...")
    elif admin_menu == 2:
        print("Loading insights...")
    else:
        main()


def load_information():
    """
    Displays information about the application when chosen
    by the user on the main menu.
    """
    reset_terminal()
    print(strings.information_text)


def cast_user_vote():
    """
    Takes validated user inputs to build list that is
    will be submitted as a vote to the external google spreadsheet.
    """
    reset_terminal()
    print(f"{Fore.MAGENTA}Welcome to the Voting Station!\n")
    print(f"{Fore.WHITE}To cast your vote, please fill out the form below\n")

    fname_input = get_voter_name("first")
    lname_input = get_voter_name("last")
    age_input = get_voter_age()
    region_input = get_voter_region()
    vote_input = get_voter_vote()
    full_vote = [fname_input, lname_input, age_input, region_input, vote_input]
    
    confirm_vote(full_vote)
    confirmation = validate_menu_selection("submit vote", "re-enter vote", "exit")
    submit_vote(confirmation, full_vote)



def get_voter_name(name_type):
    """
    Ensures that data submitted when user cast votes is correct
    and returns correct value before data is submitted to spreadsheet.
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

    name_type = name_type.capitalize()
    print(f"\n{Fore.GREEN}{name_type} Name Entered: {name}\n")
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
                print(f"\n{Fore.GREEN}Age Entered: {age}\n")
                break
            else:
                print(f"{Fore.RED}Please enter an age between 18 and 120:\n")
    
    return age


def get_voter_region():
    """
    Returns the region selected by the user in vote casting after
    input has been validated in validate_menu_selection function.
    """
    print(f"{Fore.CYAN}Please select the region you are voting from:\n")
    print(f"{Fore.WHITE}1. Eastbourne\n2. Hastings\n3. Lewes\n")
    region = validate_menu_selection("Eastbourne", "Hastings", "Lewes")

    if region == 1:
        region_selection = "Eastbourne"
    elif region == 2:
        region_selection = "Hastings"
    else:
        region_selection = "Lewes"

    print(f"\n{Fore.GREEN}Region Selected: {region_selection}\n")
    return region_selection


def get_voter_vote():
    """
    Returns the party vote selected by the user after
    input has been validated in validate_menu_selection function.
    """
    print(f"{Fore.CYAN}Please select the party that you are voting for:\n")
    print(strings.party_list)
    
    vote = validate_menu_selection("the Red Party", "the Green Party", "the Blue Party")

    if vote == 1:
        vote_selection = "Red"
    elif vote == 2:
        vote_selection = "Green"
    else:
        vote_selection = "Blue"

    print(f"\n{Fore.GREEN}Vote Chosen: The {vote_selection} Party\n")
    return vote_selection


def confirm_vote(vote):
    """
    Confirms the data input by the user when casting vote before
    submitting to the google sheet.
    """
    reset_terminal()
    print(f"{Fore.CYAN}Are you happy with the details that you have entered?\n")
    print(f"{Fore.BLUE}Name: {Fore.WHITE}{vote[0]} {vote[1]}")
    print(f"{Fore.BLUE}Age: {Fore.WHITE}{vote[2]}")
    print(f"{Fore.BLUE}Region: {Fore.WHITE}{vote[3]}")
    print(f"{Fore.BLUE}Vote: {Fore.WHITE}{vote[4]}\n")
1    


def submit_vote(answer, vote_list):
    """
    Takes the input from the validate_vote_confirm function and submits vote
    if y is selected and restarts voting process if n is selected.
    """
    if answer == 1:
        print(f"{Fore.GREEN}Vote submitted...")
        vote_sheet = SHEET.worksheet("votes")
        vote_sheet.append_row(vote_list)
        print(f"{Fore.GREEN}Loading Voter Portal...")
        load_voter_portal()
    elif answer == 2:
        cast_user_vote()
    else:
        main()


def validate_menu_selection(ch1, ch2, ch3):
    """
    Ensures that the correct input is given by the user in
    the multiple choice menu that appears throughout the
    application.
    """
    prompt = f"Press 1 for {ch1}, 2 for {ch2}, or 3 for {ch3}\n"
    while True:
        try:
            selection = int(input(f"{Fore.CYAN}{prompt}"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: {prompt}")
            continue

        if selection >= 1 and selection <= 3:
            break
        else:
            print(f"{Fore.RED}Incorrect Input: {prompt}")

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
            print(f"{Fore.GREEN}Login details correct")
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
