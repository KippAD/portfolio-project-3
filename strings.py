from colorama import Fore
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
    f"{Fore.WHITE}Cast your vote in the upcoming election between\n"
    f"{Fore.WHITE}the {Fore.RED}Red, {Fore.GREEN}Green, "
    f"{Fore.WHITE}and {Fore.BLUE}Blue {Fore.WHITE}parties.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Voter Portal\n2. Admin Portal\n3. Information\n"
    )

# The text displayed when the voter portal is loaded
voter_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Voter Portal!\n\n"
    f"{Fore.WHITE}This menu will allow you to cast a vote in the election\n"
    f"or to view the current vote count.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Cast Vote\n2. View Results\n3. Main Menu\n"
)

# The text displayed when the admin portal is loaded
admin_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Admin Portal!\n\n"
    f"{Fore.WHITE}1. Vote Results\n2. Voting Insights\n"
)

# The information displayed when the user selects information on the main menu
information_text = (
    f"{Fore.MAGENTA}Welcome to the Sussex Voting Station\n\n"
    f"{Fore.WHITE}This application is the official method of casting\n"
    f"your vote in the ongoing Sussex regional elections.\n\n"
    f"{Fore.BLUE}Candidates:\n\n"
    f"{party_list}\n"
    f"{Fore.WHITE}To cast your vote, simply head to the Voter Portal from\n"
    f"the main menu. The current vote count can also be viewed there.\n\n"
)

vote_results_text = (
    f"{Fore.MAGENTA}Welcome to the Voting Results menu\n\n"
    f"{Fore.WHITE}You can view the current vote count as well as\n"
    f"insights about the demographics of the vote by \n"
    f"selecting an option the menu below\n\n"
    f"1. Current Vote Count\n2. Voting Insights\n3. Return to Voter Portal\n"
)

insights_page_text = (
    f"{Fore.MAGENTA}Welcome to Insights\n\n"
    f"{Fore.WHITE}Here you will find actionable data regarding the election "
    f"and voter demographics in bar chart form.\n"
)

insights_age_figure = (
    f"{Fore.BLUE}The Votes by Age Bracket {Fore.WHITE}figure below shows "
    f"how the votes are split amongst various age groups.\n"
)

insights_region_figure = (
    f"{Fore.BLUE}\nThe Votes by Region {Fore.WHITE}figure below shows the "
    f"popularity of each party in the voting regions (Sussex, \n"
    f"Eastbourne, Hastings).\n"
)