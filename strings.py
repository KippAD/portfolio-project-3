"""
This file stores the larger strings that make up the applications display
and that ar accessed throughout the main run.py file.
"""
from colorama import Fore, Back
import colorama
colorama.init(autoreset=True)

# The list of parties that appears multiple times in application.
party_list = (
    f"{Fore.WHITE}1. {Fore.RED}The Red Party\n"
    f"{Fore.WHITE}2. {Fore.GREEN}The Green Party\n"
    f"{Fore.WHITE}3. {Fore.BLUE}The Blue Party\n"
)

# The text displayed when the main menu is loaded.
main_menu_text = (
    f"{Fore.MAGENTA}Welcome to the Sussex Voting Station!\n\n"
    f"{Fore.WHITE}This application is the official method of vote casting "
    f"for\nthe ongoing election between {Fore.WHITE}the {Fore.RED}Red, "
    f"{Fore.GREEN}Green, {Fore.WHITE}and {Fore.BLUE}Blue {Fore.WHITE}parties."
    f"{Fore.CYAN}\n\nPlease select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Voter Portal\n2. Admin Portal\n3. Information\n"
    )

# The text displayed when the voter portal is loaded.
voter_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Voter Portal!\n\n"
    f"{Fore.WHITE}Use this menu to cast a vote or to navigate to the\n"
    f"voting results and insights menu.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Cast Vote\n2. View Results\n3. Main Menu\n"
)

# The text displayed when the admin portal is loaded.
admin_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Admin Portal!\n\n"
    f"{Fore.WHITE}This area is locked by login and password as it handles "
    f"sensitive data\nabout voters. This portal can be used to view and"
    f" manipulate this data.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. View Votes\n2. Vote Control\n3. Return to Main Menu\n"
)

# The information displayed when the user selects information on the main menu.
information_text = (
    f"{Fore.MAGENTA}Welcome to the Sussex Voting Station\n\n"
    f"{Fore.WHITE}This application is the official method of casting your "
    f"vote\nin the ongoing Sussex regional elections.\n\n"
    f"Throughout the application users may also view information regarding \n"
    f"the status of the vote as well as insights about voting demographics.\n"
    f"\n{Fore.BLUE}Candidates:\n\n"
    f"{party_list}\n"
    f"{Fore.WHITE}To cast a vote simply head to the Voter Portal from "
    f"the main\nmenu. The insights menu may also be accessed from there.\n"
)

# The msg presented to the user when they try to cast a vote and voting is
# toggled off by the admin.
voting_disabled_text = (
    f"{Fore.RED}Sorry, voting has been disabled for the time being...\n\n"
    f"{Fore.WHITE}This could be just a temporary measure, so please try again "
    f"later.\nIn the meantime feel free to view the vote count and voting "
    f"insights\nin the Vote Results menu."
)

# The text displayed in the voting results area.
vote_results_text = (
    f"{Fore.MAGENTA}Welcome to the Voting Results menu\n\n"
    f"{Fore.WHITE}Here you can view the current vote count and certain "
    f"insights\nabout the demographics of the vote by using the menu below.\n"
    f"\n1. Current Vote Count\n2. Voting Insights\n3. Return to Voter Portal\n"
)

# Main text displayed in the insights area of the application.
insights_page_text = (
    f"{Fore.MAGENTA}Welcome to Insights\n\n"
    f"{Fore.WHITE}This area contains actionable insights about the "
    f"demographics of voters in the\nelection and can be used to "
    f"understand trends in voting.\n\n"
)

# Annotation for the first bar chart in the insights area.
insights_age_figure = (
    f"{Fore.BLUE}The Votes by Age Bracket {Fore.WHITE}figure below shows "
    f"how the votes are split amongst\nvarious age groups. (Note: If there is "
    f"an issue with the bar chart\nthen return to the results menu and reload "
    f"the insights page).\n"
)

# Annotation for the second bar chart in the insights area.
insights_region_figure = (
    f"{Fore.BLUE}\nThe Votes by Region {Fore.WHITE}figure below shows the "
    f"popularity of each party in the\nvoting regions (Sussex, "
    f"Eastbourne, Hastings).\n"
)

# Displays the text above the table in the admin portal vote results area.
admin_votes_text = (
    f"{Fore.MAGENTA}Welcome Admin!\n\n"
    f"{Fore.WHITE}The full list of votes are printed above - be mindful that "
    f"voter names \nmust remain anonymous.\n\n"
    f"{Fore.CYAN}As admin you have the power to delete votes.\n\n"
    f"{Fore.RED}Note: This action is irreversible and should only be done\n"
    f"if a vote is deemed illegitimate..."
)

# Text that makes up the title of the vote table in the admin portal (irregular
# spacing is used to match up title with each column in table).
admin_votes_titles = (
    f"{Back.YELLOW}{Fore.BLACK}\nNo. FName:       SName:       Age:"
    f"Region:     Vote: "
)

# The text printed in the control menu where the admin can toggle whether
# votes can be cast or not.
admin_control_text = (
    f"{Fore.MAGENTA}Welcome to the Voting Control Switch!\n\n"
    f"{Fore.WHITE}Use this switch to disable vote casting when the election "
    f"is over,\nif there is an issue with the system, or if suspicious data "
    f"is being\nsubmitted to the database.\n"
)

# Delete vote confirmation prompt in the vote section of the admin portal.
delete_prompt = (
        f"Please enter the vote number of the vote that you wish\n"
        f"to delete, to cancel this action press 0:"
    )

# Two states of switch in admin control that print if voting is on or off.
vote_toggle_on = f"{Back.GREEN}{Fore.BLACK}Voting is currently switched ON"
vote_toggle_off = f"{Back.RED}{Fore.BLACK}Voting is currently switched OFF"
