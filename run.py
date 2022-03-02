import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from termcolor import cprint 
from pyfiglet import figlet_format

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_voting_system')


