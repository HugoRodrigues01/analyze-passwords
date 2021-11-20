
# Imports 
from rich import print, table, console, progress
from time import sleep
from typing import List
from utils import SPACIAL_CHARACTER, randoming_password, credits
import os

# Crianting the console
console_main: console.Console = console.Console()

def version() -> None:
    print()
    print("-" * 50)
    print("Version: [blue bold]0.0.0[/]v")
    print("-" * 50)

def cheking_the_password(password: str) -> None:
    """
    This function will cheking your password.
    """

    count_special_character: int = 0
    count_len: int = len(password)
    exists_spacial_character: bool = False
    exists_number: bool = False
    count_numbers: int = 0
    status: str = ""
    points: int = 0
    exists_uppercase_letter: bool = False

    # Progress bar
    # count the points for the password
    print()
    for letter in progress.track(password, "Verify your password..."):
        if letter in ["@", "!", "#", "%", "*", "&", ">", "<", "¨"]:
            
            count_special_character += 1
            exists_spacial_character = True
        
        if letter.isupper():
            exists_uppercase_letter = True
        
        else:
            try:
                int(letter)
                count_numbers += 1
            except ValueError:
                pass
            else:
                exists_number = True

        sleep(0.5)
        
    if exists_number:
        points += 2

    if exists_spacial_character and count_special_character >= 3:
        points += 5

    elif count_special_character < 3:
        points += 2

    if exists_uppercase_letter:
        points += 4

    if 1 < points <= 7:
        status = "[red]Password weak[/] :x:"

    elif 8 <= points <= 10:
        status = "[yellow]Password reasonable[/]"

    elif points > 10:
        status = "[green]Password strong[/] :white_check_mark:"

    print("[green]=[/]" * 50)
    print(
        f"Exists spacial characters.................... {exists_spacial_character}\n"
        f"Exists numbers:.............................. {exists_number}\n"
        f"The amount spacial characters:............... {count_special_character}\n"
        f"The amount of numbers:....................... {count_numbers}\n"
        f"Len of password:............................. {count_len}\n\n"
        f"Status: {status}"
    )
    print("[green]=[/]" * 50)


def verify_password() -> None:
    
    print()
    password: str = console_main.input("Type your [bold]password[/] [green]>>>[/] ")

    # Verifing, if the password has the least sixteen digits.
    while len(password) < 16:
        print()
        print("[red]Your password must be at least [blue]16[/] digits long.[/]\nPleas type your password again.\n")

        password = console_main.input("[bold]Your password[/] [green]>>>[/] ")
    
    # Calling the verify the password
    cheking_the_password(password)

def main() -> None:

    print("[green]=[/]" * 50)
    print("[bold]Analize Passwords[/] :lock:".center(60))
    print("[green]=[/]" * 50)

    print("-" * 50)
    print(
        "1 - Verify your password :white_check_mark:\n"
        "2 - Creating a new random password\n"
        "3 - Credits\n"
        "6 - Exit :x:"
    )
    print("-" * 50)

    VALID_OPTIONS: List[str] = ["1", "2", "3", "6"]

    option: str = console_main.input("Type an option above [green]>>>[/] ")

    while option not in VALID_OPTIONS:
        print()
        print("[red]Your option is invalid!, type an option valid.[/]")

        option = console_main.input("Your option [green]>>>[/] ")
    
    match option:
        case "1":
            verify_password()

        case "2": pass
        case "3": pass

        case "6":
            # Closing the program
            exit(0)
        

if __name__ == "__main__":
    main()

