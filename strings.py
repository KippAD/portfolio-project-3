from colorama import Fore
import colorama
colorama.init(autoreset=True)

# This file stores the larger strings that make up the applications
# display and can be accessed in the main run.py file.

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

admin_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Admin Portal!\n\n"
    f"{Fore.WHITE}1. Vote Results\n2. Voting Insights\n"
)
