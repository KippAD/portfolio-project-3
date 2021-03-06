"""Main file that runs the voting station application"""
import time
import os
import collections
from tabulate import tabulate
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import Fore
from google.oauth2.service_account import Credentials
import plotext as plt
import gspread
import colorama
import strings
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
    Displays main menu with possible navigation options and takes user input
    to navigate to chosen area of application.
    """
    loading_message("the Main Menu")
    print(strings.main_menu_text)

    msg = "Press 1 for voter portal, 2 for admin portal, or 3 for information:"
    chosen_portal = validate_three_options(msg)
    if chosen_portal == 1:
        load_voter_portal()
    elif chosen_portal == 2:
        load_admin_portal()
    else:
        load_information()


def load_voter_portal():
    """
    Displays the voter portal with possible navigation options and takes
    user input to navigate to chosen area of application.
    """
    loading_message("the Voter Portal")
    print(strings.voter_portal_text)

    msg = "Press 1 to cast a vote, 2 to view vote results or 3 for main menu:"
    voter_menu = validate_three_options(msg)
    if voter_menu == 1:
        check_voting_status()
    elif voter_menu == 2:
        vote_results_menu()
    else:
        main()


def load_information():
    """
    When selected from the main menu the function displays the information area
    which explains the applications purpose to the user.
    """
    loading_message("Information")
    print(strings.information_text)
    load_main_menu()


def check_voting_status():
    """
    Checks google sheet to see if voting is switched on or off and will block
    voting if cell value is off. Explains to the user that voting is disabled
    and offers option to return to voter portal.
    """
    voting_switch = SHEET.worksheet("control").acell("A2").value
    if voting_switch == "on":
        load_vote_casting()
    else:
        reset_terminal()
        print(f"{strings.voting_disabled_text}")
        input(f"{Fore.CYAN}\nEnter any key to return to the Voter Portal:\n")
        load_voter_portal()


def load_vote_casting():
    """
    Instigates the vote casting process but first gives user an option to
    return to the voter portal.
    """
    loading_message("Vote Casting")
    print(f"{Fore.MAGENTA}Welcome to the Voting Station!")

    prompt = "Press 1 to begin voting, press 2 to return to the voter portal:"
    response = validate_two_options(prompt)
    if response == 1:
        cast_user_vote()
    elif response == 2:
        load_voter_portal()


def cast_user_vote():
    """
    Takes validated user inputs to build a list that will be submitted as a
    vote to the external google spreadsheet.
    """
    reset_terminal()
    print(f"{Fore.WHITE}To cast your vote, please fill out the form below\n")
    # Takes inputs for both names and resets terminal
    fname_input = get_voter_name("first")
    lname_input = get_voter_name("last")
    time.sleep(2)
    reset_terminal()
    # Gathers inputs for age and region and resets terminal
    age_input = get_voter_age()
    region_input = get_voter_region()
    time.sleep(2)
    reset_terminal()
    # Gets party vote and loads vote confirmation display
    vote_input = get_voter_vote()
    time.sleep(2)
    full_vote = [fname_input, lname_input, age_input, region_input, vote_input]
    confirm_vote(full_vote)
    # Takes user input to confirm vote submission
    msg = "Press 1 to submit your vote, 2 start again, or 3 for voter portal:"
    confirmation = validate_three_options(msg)
    submit_vote(confirmation, full_vote)


def get_voter_name(name_type):
    """
    Gets name input for vote casting and ensures that input data submitted by
    user is correct before returning the validated value.
    """
    error = "Please exclude any numbers, spaces, or special characters..."
    input_prompt = f"Please enter your {name_type} name:"

    while True:
        name = input(f"{Fore.CYAN}{input_prompt}{Fore.WHITE}\n")
        name = name.title()

        if name.isalpha():
            break
        else:
            print(f"{Fore.RED}\nYour name can only contain letters.\n")
            print(f"{error}\n")
            continue

    name_type = name_type.capitalize()
    print(f"\n{Fore.GREEN}{name_type} Name Entered: {name}\n")
    return name


def get_voter_age():
    """
    Gets voters age from an input, validates that the value is an integer
    between 18 and 120 before returning the value.
    """
    input_prompt = "Please enter your age:"

    while True:
        try:
            age = int(input(f"{Fore.CYAN}{input_prompt}{Fore.WHITE}\n"))
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
    Returns the region selected by the user in vote casting after input has
    been validated in validate_three_options function.
    """
    print(f"{Fore.CYAN}Please select the region you are voting from:\n")
    print(f"{Fore.WHITE}1. Eastbourne\n2. Hastings\n3. Lewes\n")
    msg = "Press 1 for Eastbourne, 2 for Hastings, or 3 for Lewes:"
    region = validate_three_options(msg)

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
    Returns the party vote selected by the user after input has been validated
    in validate_three_options function.
    """
    print(f"{Fore.CYAN}Please select the party that you are voting for:\n")
    print(strings.party_list)

    msg = (
        "Press 1 for the Red Party, 2 for the Green Party, or 3 for the "
        "Blue Party:"
    )
    vote = validate_three_options(msg)

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
    Prints all data input by the user during vote casting for the purposes
    of vote confirmation in the submit_vote function.
    """
    reset_terminal()
    print(f"{Fore.CYAN}Are you happy with the information entered?\n")
    print(f"{Fore.BLUE}Name: {Fore.WHITE}{vote[0]} {vote[1]}")
    print(f"{Fore.BLUE}Age: {Fore.WHITE}{vote[2]}")
    print(f"{Fore.BLUE}Region: {Fore.WHITE}{vote[3]}")
    print(f"{Fore.BLUE}Vote: {Fore.WHITE}{vote[4]}\n")


def submit_vote(answer, vote_list):
    """
    Takes parameters from cast_user_vote function and takes appropriate action
    depending on input - 1 submits vote to google sheet, 2 begins voting
    process again, and 3 cancels vote submission and reloads voter portal.
    """
    if answer == 1:
        print(f"{Fore.GREEN}Vote submitted...")
        vote_sheet = SHEET.worksheet("votes")
        vote_sheet.append_row(vote_list)
        time.sleep(1)
        load_voter_portal()
    elif answer == 2:
        cast_user_vote()
    else:
        load_voter_portal()


def vote_results_menu():
    """
    Displays the results menu with options to either view vote count, view
    different insights about the voting results, or return to voter portal.
    Takes input and navigates user to correct area.
    """
    loading_message("the Vote Results Menu")
    print(strings.vote_results_text)

    msg = "Press 1 for vote results, 2 for insights, or 3 for voter portal:"
    choice = validate_three_options(msg)

    if choice == 1:
        load_vote_percentage()
    elif choice == 2:
        load_voting_insights()
    else:
        load_voter_portal()


def load_vote_percentage():
    """
    Gets votes from google sheet and counts them before converting them into
    percentages. Then organizes data in the correct way to be passed through
    display_vote_percentage function.
    """
    # Gets votes from google sheet
    party_votes = SHEET.worksheet("votes").col_values(5)
    party_votes.pop(0)
    # Converts votes into a percentage after counting them
    counted = count_votes(party_votes)
    red_percent = calculate_percentage(counted[0], counted[1])
    green_percent = calculate_percentage(counted[0], counted[2])
    blue_percent = calculate_percentage(counted[0], counted[3])
    # Converts vote data into correct format for bar chart display
    chart_headings = ["Red Party", "Green Party", "Blue Party"]
    chart_percentage = [red_percent, green_percent, blue_percent]
    display_vote_percentage(chart_headings, chart_percentage, counted)


def count_votes(total_votes):
    """
    Counts the votes from the google sheet and returns a list with the total
    count and the count of each of the three parties.
    """
    total_count = len(total_votes)
    # Counts occurences of each vote in party_votes list
    count = collections.Counter(total_votes)
    votes_list = [total_count, count["Red"], count["Green"], count["Blue"]]

    return votes_list


def display_vote_percentage(headings, percentage, count):
    """
    Displays the bar chart using data provided from load_vote_percentage
    function and also prints text into the current vote count area.
    """
    loading_message("the Vote Count")
    print("This is the current vote count of the election:")
    print(f"{Fore.RED}The Red Party: {percentage[0]}% ({count[1]} Votes)")
    print(f"{Fore.GREEN}The Green Party: {percentage[1]}% ({count[2]} Votes)")
    print(f"{Fore.BLUE}The Blue Party: {percentage[2]}% ({count[3]}) Votes")
    plt.bar(headings, percentage, orientation="h")
    plt.xlim(0, 70)
    plt.plot_size(100, 20)
    plt.title("Current Vote Count Percentage")
    plt.cls()
    plt.show()
    load_results_menu()


def load_voting_insights():
    """
    Displays bar charts of voting popularity by age and region in insights
    area, allowing user to see the demographics of party supporters.
    """
    loading_message("Voting Insights")
    # Converts ages in google sheet from string into integer
    ages_str = SHEET.worksheet("votes").col_values(3)
    ages_str.pop(0)
    ages_list = [int(a) for a in ages_str]
    # Collects regions from google sheet
    regions_list = SHEET.worksheet("votes").col_values(4)
    regions_list.pop(0)
    # Collects votes from google sheet
    votes_list = SHEET.worksheet("votes").col_values(5)
    votes_list.pop(0)
    # Passes lists into unique counting functions
    reset_terminal()
    print(f"{strings.insights_page_text}")
    print(f"{strings.insights_age_figure}")
    count_age_votes(votes_list, ages_list)
    time.sleep(1)
    print(f"{strings.insights_region_figure}")
    count_region_votes(votes_list, regions_list)
    load_results_menu()


def count_age_votes(votes, ages):
    """
    Categorizes votes into age groups to pass through display_insights_chart
    function which displays a bar chart in the insights area.
    """
    # Creates lists of each age bracket to be displayed in insights
    below_30 = [x for ind, x in enumerate(votes) if ages[ind] < 30]
    below_50 = [x for ind, x in enumerate(votes) if ages[ind] in range(31, 51)]
    below_70 = [x for ind, x in enumerate(votes) if ages[ind] in range(51, 71)]
    above_70 = [x for ind, x in enumerate(votes) if ages[ind] >= 71]

    # Data passed into the display_insights_chart function to fill in bar chart
    age_title = "Votes by Age Bracket(Percentage)"
    age_subheadings = ["18-30", "31-50", "51-70", "70+"]
    age_data = [below_30, below_50, below_70, above_70]
    display_insights_chart(age_title, age_subheadings, age_data)


def count_region_votes(votes, region):
    """
    Categorizes votes into regions voted from to pass through
    display_insights_chart function which displays a second bar chart in the
    insights area.
    """
    # Creates lists of votes for each region to be counted later
    lewes = [x for ind, x in enumerate(votes) if region[ind] == "Lewes"]
    eastb = [x for ind, x in enumerate(votes) if region[ind] == "Eastbourne"]
    hast = [x for ind, x in enumerate(votes) if region[ind] == "Hastings"]

    # Data passed into the display_insights_chart function to fill in bar chart
    region_title = "Votes by Region(Percentage)"
    region_subheadings = ["Lewes", "Eastbourne", "Hastings"]
    region_data = [lewes, eastb, hast]
    display_insights_chart(region_title, region_subheadings, region_data)


def display_insights_chart(chart_title, chart_subheadings, chart_data):
    """
    Takes parameters from count_age_votes and count_region_votes functions in
    order to display a bar chart, this includes converting the lists of votes
    into percentages.
    """
    red_percentages = []
    green_percentages = []
    blue_percentages = []
    # Appends above lists with counted percentages of each party
    for ind in chart_data:
        counted = count_votes(ind)
        red_percentages.append(calculate_percentage(counted[0], counted[1]))
        green_percentages.append(calculate_percentage(counted[0], counted[2]))
        blue_percentages.append(calculate_percentage(counted[0], counted[3]))
    # New lists are used to plot chart below
    plt.multiple_bar(
        chart_subheadings,
        [blue_percentages, green_percentages, red_percentages],
        label=["Blue", "Green", "Red"]
        )
    plt.title(f"{chart_title}")
    plt.plot_size(100, 25)
    plt.show()
    plt.clf()
    plt.cld()


def load_admin_portal():
    """
    Instigates loading the admin portal and will only call display_admin_portal
    function once login has passed through validate_admin_login function.
    """
    loading_message("Admin Login")
    print(f"{Fore.CYAN}You must login to access the admin portal.\n")
    validate_admin_login()
    display_admin_portal()


def validate_admin_login():
    """
    Asks the user to enter the admin and password required to access the admin
    portal and ensures that login details are correct before allowing access.
    """
    username = "admin"
    password = "password"

    while True:
        reset_terminal()
        print(f"{Fore.MAGENTA}You must log in to access the Admin Portal!")
        # Option for user to exit out of login at the start of each loop.
        prompt = "Press 1 to login, or 2 to return to the main menu:"
        selection = validate_two_options(prompt)
        if selection == 2:
            main()

        un_in = input(f"{Fore.CYAN}Please enter the username:\n{Fore.WHITE}")
        pw_in = input(f"{Fore.CYAN}Please enter the password:\n{Fore.WHITE}")
        if un_in == username and pw_in == password:
            print(f"\n{Fore.GREEN}Login details correct")
            break
        else:
            print(f"{Fore.RED}Incorrect login")
            time.sleep(2)


def display_admin_portal():
    """
    Displays the admin menu once login is correctly completed. Displays options
    to view vote results and voting insights and takes user input to navigate
    to selected area.
    """
    loading_message("the Admin Portal")
    print(strings.admin_portal_text)

    msg = "Press 1 to view all votes, 2 for admin control, or 3 for main menu:"
    admin_menu = validate_three_options(msg)
    if admin_menu == 1:
        load_admin_votes()
    elif admin_menu == 2:
        load_admin_control()
    else:
        main()


def load_admin_votes():
    """
    Displays all votes from google sheet into console in tabular form,
    including sensitive data that is not accessible in user area.
    """
    loading_message("Vote Data")
    sheet = SHEET.worksheet("votes")
    vote_rows = sheet.get_all_values()
    vote_rows.pop(0)
    i = 1
    for rows in vote_rows:
        rows.insert(0, i)
        i += 1

    print(f"{strings.admin_votes_titles}")
    print(tabulate(vote_rows))
    print(f"{strings.admin_votes_text}")
    get_admin_actions()


def get_admin_actions():
    """
    Presents admin with possible actions when on the admin votes display,
    including the option to delete a row.
    """
    prompt = "Press 1 to delete a vote, or 2 to return to the Admin Portal:"
    action = validate_two_options(prompt)

    if action == 1:
        delete_vote()
    else:
        display_admin_portal()


def delete_vote():
    """
    Takes an integer input from the admin and validates that it is a number
    within the range of the length of all vote indexes. Calls
    confirm_vote_deletion function if valid number is entered.
    """
    total = SHEET.worksheet("votes").col_values(1)
    prompt = f"{strings.delete_prompt}"
    while True:
        try:
            delete_num = int(input(f"\n{Fore.CYAN}{prompt}{Fore.WHITE}\n"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: {prompt}")
            continue
        else:
            if delete_num in range(1, len(total)):
                # Passes chosen vote into delete confirmation
                confirm_vote_deletion(delete_num)
                break
            elif delete_num == 0:
                print(f"{Fore.GREEN}Action cancelled...")
                load_admin_votes()
            else:
                print(f"{Fore.RED}{delete_num} is not a valid vote number...")


def confirm_vote_deletion(vote_index):
    """
    Takes the integer provided in the delete vote function to delete a vote
    from the printed table in the admin votes area, also offering an option
    to cancel the action and reload the area.
    """
    print(f"{Fore.RED}Are you sure? Vote deletion is permanent...")
    prompt = "Press 1 to confirm or 2 to cancel:"
    confirm = validate_two_options(prompt)

    if confirm == 1:
        # Uses delete + 1 to match the no. with the google sheet row
        SHEET.worksheet("votes").delete_rows(vote_index + 1)
        print(f"{Fore.GREEN}Vote deleted...")
        time.sleep(2)
        load_admin_votes()
    else:
        print(f"{Fore.RED}Vote deletion cancelled...")
        load_admin_votes()


def load_admin_control():
    """
    Displays the menu text where admin can disable voting in application and
    takes user input to toggle vote switch.
    """
    loading_message("Admin Control")
    print(f"{strings.admin_control_text}")

    toggle_state = SHEET.worksheet("control").acell("A2").value
    if toggle_state == "on":
        print(f"{strings.vote_toggle_on}")
    else:
        print(f"{strings.vote_toggle_off}")

    prompt = "Press 1 to toggle the voting, or 2 to return to admin portal:"
    response = validate_two_options(prompt)

    if response == 1:
        lock_voting_admin(toggle_state)
    else:
        display_admin_portal()


def lock_voting_admin(switch_state):
    """
    Alters the switch value in google sheet when administrator toggles voting
    on or off annd then reloads the admin control area with updated value.
    """
    if switch_state == "on":
        SHEET.worksheet("control").update("A2", "off")
        print(f"\n{Fore.RED}Switching voting off...")
    else:
        SHEET.worksheet("control").update("A2", "on")
        print(f"\n{Fore.GREEN}Switching voting on...")

    time.sleep(2)
    load_admin_control()


def validate_two_options(input_msg):
    """
    Validates the input given by a user when there is an input with two
    possible options, returning the value once validation has finished.
    """
    while True:
        try:
            decision = int(input(f"\n{Fore.CYAN}{input_msg}{Fore.WHITE}\n"))
        except ValueError:
            print(f"{Fore.RED}Incorrect Input: {input_msg}{Fore.WHITE}")
            continue
        else:
            if decision == 1 or decision == 2:
                break
            else:
                print(f"{Fore.RED}Incorrect Input: {input_msg}{Fore.WHITE}")

    return decision


def validate_three_options(input_msg):
    """
    Validates the input given by a user when there is an input with three
    possible options, returning the value once validation has finished.
    """
    while True:
        try:
            selection = int(input(f"{Fore.CYAN}{input_msg}\n{Fore.WHITE}"))
        except ValueError:
            print(f"{Fore.RED}Error: Your input must be a number.\n")
            continue
        else:
            if selection >= 1 and selection <= 3:
                break
            else:
                print(f"{Fore.RED}Error: Your input must be 1 or 2\n")

    return selection


def loading_message(area):
    """
    Prints the loading msg that is displayed when moving throughout areas of
    the application before clearing the terminal.
    """
    print(f"\n{Fore.BLUE}Loading {area}....\n")
    time.sleep(1.5)
    reset_terminal()


def calculate_percentage(total, count):
    """
    Calculates the percentage of a value to two decimal places.
    """
    percentage = count / total * 100
    percentage = round(percentage, 2)
    return percentage


def load_main_menu():
    """
    Allows user to enter any input to be redirected to main menu.
    """
    input_prompt = "Enter any key to return to the main menu:"
    input(f"{Fore.CYAN}\n{input_prompt}{Fore.WHITE}\n")
    main()


def load_results_menu():
    """
    Allows user to enter any input to be redirected to results menu.
    """
    input_prompt = "Enter any key to return to the results menu"
    input(f"{Fore.CYAN}\n{input_prompt}{Fore.WHITE}\n")
    vote_results_menu()


def reset_terminal():
    """
    Clears the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('printf "\ec"')
    title = "The Voting Station!"
    cprint(figlet_format(title, font='big'), "green", attrs=["bold"])


def main():
    """
    The main function where all application functions run.
    """
    display_main_menu()


main()
