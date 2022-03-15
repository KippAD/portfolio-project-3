from colorama import Fore, Back
import colorama
colorama.init(autoreset=True)

# This file stores the larger strings that make up the applications
# display and can be accessed in the main run.py file.

# The list of parties that appears multiple times in application
party_list = (
    f"{Fore.WHITE}1. {Fore.RED}The Red Party\n"
    f"{Fore.WHITE}2. {Fore.GREEN}The Green Party\n"
    f"{Fore.WHITE}3. {Fore.BLUE}The Blue Party\n"
)

# The text displayed when the main menu is loaded
main_menu_text = (
    f"{Fore.MAGENTA}Welcome to the Sussex Voting Station!\n\n"
    f"{Fore.WHITE}This application is the official method of vote casting "
    f"for\nthe ongoing election between {Fore.WHITE}the {Fore.RED}Red, "
    f"{Fore.GREEN}Green, {Fore.WHITE}and {Fore.BLUE}Blue {Fore.WHITE}parties."
    f"{Fore.CYAN}\n\nPlease select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Voter Portal\n2. Admin Portal\n3. Information\n"
    )

# The text displayed when the voter portal is loaded
voter_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Voter Portal!\n\n"
    f"{Fore.WHITE}Use this menu to cast a vote or to navigate to the\n"
    f"voting results and insights menu.\n\n"
    f"In the wrong place? Head back to the Main Menu by pressing 3.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Cast Vote\n2. View Results\n3. Main Menu\n"
)

# The text displayed when the admin portal is loaded
admin_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Admin Portal!\n\n"
    f"{Fore.WHITE}This area is locked by login and password as it handles "
    f"sensitive data\nabout voters. This portal can be used to view and"
    f" manipulate this data.\n\n"
    f"{Fore.WHITE}1. View Votes\n2. End Vote\n3. Return to Main Menu\n"
)

# The information displayed when the user selects information on the main menu
information_text = (
    f"{Fore.MAGENTA}Welcome to the Sussex Voting Station\n\n"
    f"{Fore.WHITE}This application is the official method of casting your vote\n"
    f"in the ongoing Sussex regional elections.\n\n"
    f"Throughout the application users may also view information regarding the\n"
    f"status of the vote as well as insights about voting demographics.\n\n"
    f"{Fore.BLUE}Candidates:\n\n"
    f"{party_list}\n"
    f"{Fore.WHITE}To cast a vote simply head to the Voter Portal from\n"
    f"the main menu. The insights menu may also be accessed from there.\n"
)

vote_results_text = (
    f"{Fore.MAGENTA}Welcome to the Voting Results menu\n\n"
    f"{Fore.WHITE}Here you can view the current vote count and certain "
    f"insights\nabout the demographics of the vote by using the menu below.\n\n"
    f"1. Current Vote Count\n2. Voting Insights\n3. Return to Voter Portal\n"
)

insights_page_text = (
    f"{Fore.MAGENTA}Welcome to Insights\n\n"
    f"{Fore.WHITE}This area contains actionable insights about the "
    f"demographics of voters in the election and can\nbe used to "
    f"understand trends in voting.\n\n"
)

insights_age_figure = (
    f"{Fore.BLUE}The Votes by Age Bracket {Fore.WHITE}figure below shows "
    f"how the votes are split amongst various age groups.\n"
)

insights_region_figure = (
    f"{Fore.BLUE}\nThe Votes by Region {Fore.WHITE}figure below shows the "
    f"popularity of each party in the voting regions\n(Sussex, "
    f"Eastbourne, Hastings).\n"
)

admin_votes_text = (
    f"{Back.YELLOW}{Fore.BLACK}\nNo.    First Name:    Second Name:    "
    "Age:    Region:   Vote:  "
)