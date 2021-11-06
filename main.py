
# Imports 
from threading import Condition
from rich import print, table, console, progress
from time import sleep
from typing import List

# Crianting the console
console_main: console.Console = console.Console()

def verify_password() -> None:
    
    print()
    password: str = console_main.input("Type your [bold]password[/] [green]>>>[/] ")

    # Verifing, if the password has the least sixteen digits.
    while len(password) < 16:
        print()
        print("[red]Your password must be at least [blue]16[/] digits long.[/]\nPleas type your password again.\n")

        password = console_main.input("[bold]Your password[/] [green]>>>[/] ")

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

