import random
from typing import List
from rich import print

SPACIAL_CHARACTER: List[str] = [
    "!", "@", "$", "%", "¨", "&", "*", "+", "_", "-",
    "ç", ";", ",", "."
    ]

NUMBERS: List[int] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

LETTERS: List[str] = [
    "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H",
    "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P",
    "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "x", "X", "w", "W", "y", "Y",
    "z", "Z"
    ]

def randoming_password() -> str:
    password: str = ""
    
    for _ in range(random.randint(16, 32)):

        match random.randint(1, 3):
            case 1:
                password += random.choice(SPACIAL_CHARACTER)
            case 2:
                password += random.choice(NUMBERS)
            case 3:
                password += random.choice(LETTERS)

    return password

def credits() -> None:

    print()
    print("""
    ----------------------------------------------------------------------------------------------------------
    hello my name is hugo rodrigues pereira, and i created a repository with a password analysis program.
        This repository is avalible on GitHub, for you download it, and study it.

    :dolls: Follow me on my github >>> https://github.com/HugoRodrigues01
 
    [red]NOTE: this program will have problems on windows, as it was created for the linux operating system.[/]
    -----------------------------------------------------------------------------------------------------------
    """)
    print()
