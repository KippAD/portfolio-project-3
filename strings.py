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
    f"{Fore.CYAN}Please select your portal:\n\n"
    f"{Fore.WHITE}1. Voter Portal\n2. Admin Portal\n"
    )

# The text displayed when the voter portal is loaded
voter_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Voter Portal!\n\n"
    f"{Fore.WHITE}Selecting 1 will begin the voting process, \n"
    f"selecting 2 will allow you to view the current\n"
    f"vote count election.\n\n"
    f"{Fore.CYAN}Please select an option from the menu below:\n\n"
    f"{Fore.WHITE}1. Cast Vote\n2. View Results\n"
)

admin_portal_text = (
    f"{Fore.MAGENTA}Welcome to the Admin Portal!\n\n"
    "1. Vote Results\n2. Voting Insights\n"
)