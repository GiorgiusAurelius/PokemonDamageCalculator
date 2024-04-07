from pyfiglet import figlet_format
from termcolor import cprint

class CLIHandler():
    
    def __init__(self) -> None:
        self.print_logo()   

    def print_logo(self):
        print()
        logo = figlet_format('PDC', font='isometric3')
        cprint(logo, 'light_magenta')

class colors():
    """Class that contains the ansi strings representing different colors
    """
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN = '\u001b[36m'
    WHITE = '\u001b[37m'
    BRIGHT_RED = '\u001b[31;1m'
    BRIGHT_GREEN = '\u001b[32;1m' 
    BRIGHT_YELLOW = '\u001b[33;1m'
    BRIGHT_BLUE = '\u001b[34;1m'
    BRIGHT_MAGENTA = '\u001b[35;1m'
    BRIGHT_CYAN = '\u001b[36;1m'
    RESET = '\u001b[0m'

if __name__ == '__main__':
    ch = CLIHandler()
    