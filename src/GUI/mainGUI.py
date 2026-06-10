from termcolor import colored
from abc import ABC, abstractmethod
import os

class MainGUI(ABC):
    
    def __init__(self):
        self.title = """
                                                                                                                                            
    ,ad8888ba,                                                                                                            88              
    d8"'    `"8b                                          ,d                                                               ""              
    d8'                                                    88                                                                               
    88             8b,dPPYba,  8b       d8  8b,dPPYba,   MM88MMM   ,adPPYba,   88,dPYba,,adPYba,   ,adPPYYba,  8b,dPPYba,   88  ,adPPYYba,  
    88             88P'   "Y8  `8b     d8'  88P'    "8a    88     a8"     "8a  88P'   "88"    "8a  ""     `Y8  88P'   `"8a  88  ""     `Y8  
    Y8,            88           `8b   d8'   88       d8    88     8b       d8  88      88      88  ,adPPPPP88  88       88  88  ,adPPPPP88  
    Y8a.    .a8P  88            `8b,d8'    88b,   ,a8"    88,    "8a,   ,a8"  88      88      88  88,    ,88  88       88  88  88,    ,88  
    `"Y8888Y"'   88              Y88'     88`YbbdP"'     "Y888   `"YbbdP"'   88      88      88  `"8bbdP"Y8  88       88  88  `"8bbdP"Y8  
                                d8'      88                                                                                              
                                d8'       88                                                                                              
    """
    
    def print_colored(self, txt : str, color : str = "white"):
        print(colored(txt, color=color))
    
    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def print_options(self):
        self.clear_terminal()
        self.print_colored(self.title, "cyan")
        self.print_colored("Encode Your Message!", "yellow")
        self.print_colored("01 <Caesar Cipher>\n02 <Vigenere Cipher>\n03 <Hash Cipher>\n04 <Rot13 Cipher>\n05 <Hex Cipher>\n06 <Binary Cipher>\n", "magenta")

    def ask(self) -> str | int:
        try:
            answer = input(colored("--> ", "light_yellow"))
            if answer.isdigit():
                return int(answer)
            elif answer.strip() != "" : return answer
        except KeyboardInterrupt:
            exit(0)

    @abstractmethod
    def run(self):
        pass
