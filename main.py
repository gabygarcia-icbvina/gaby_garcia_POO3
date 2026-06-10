from src.lib.cryptomania import CryptoMania
from src.GUI.mainGUI import MainGUI

class Main(MainGUI):

    def __init__(self):
        super().__init__()
        
    def run(self):
        self.print_options()
        question = self.ask()
        if question == 1:
            self.print_colored("Now enter the message and shifts of the cypher", "magenta")
            caesar_msg = self.ask()
            caesar_shift = self.ask()
            if caesar_msg.strip() != "" and isinstance(caesar_shift, int):
                Caesar = CryptoMania("Caesar", caesar_msg, caesar_shift)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif caesar_msg.strip() == "":
                raise ValueError("The Message must not be empty")
            elif not isinstance(caesar_shift, int):
                raise ValueError("The shifts must be a int")
            
        elif question == 2:
            self.print_colored("Now enter the message and key of the cypher", "magenta")
            vigenere_msg = self.ask()
            vigenere_key = self.ask()
            if vigenere_msg.strip() != "" and isinstance(vigenere_key, str):
                Caesar = CryptoMania("Vigenere", vigenere_msg, key=vigenere_key)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif vigenere_msg.strip() == "":
                raise ValueError("The Message must not be empty")
            
            elif not isinstance(vigenere_key, str):
                raise ValueError("The key must be a string")
        
        elif question == 3:
            self.print_colored("Now enter the message of the cypher", "magenta")
            hash_msg = self.ask()
            if hash_msg.strip() != "":
                Caesar = CryptoMania("Hash", hash_msg)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif hash_msg.strip() == "":
                raise ValueError("The Message must not be empty")
        
        elif question == 4:
            self.print_colored("Now enter the message of the cypher", "magenta")
            rot13_msg = self.ask()
            if rot13_msg.strip() != "":
                Caesar = CryptoMania("Rot13", rot13_msg)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif rot13_msg.strip() == "":
                raise ValueError("The Message must not be empty")
            
        elif question == 5:
            self.print_colored("Now enter the message of the cypher", "magenta")
            hex_msg = self.ask()
            if hex_msg.strip() != "":
                Caesar = CryptoMania("Hex", hex_msg)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif hex_msg.strip() == "":
                raise ValueError("The Message must not be empty")
        
        elif question == 6:
            self.print_colored("Now enter the message of the cypher", "magenta")
            binary_msg = self.ask()
            if binary_msg.strip() != "":
                Caesar = CryptoMania("Binary", binary_msg)
                Caesar.printMessage()
                self.print_colored("---", "yellow")
                Caesar.run()
                Caesar.printMessage()
                exit(0)
            elif binary_msg.strip() == "":
                raise ValueError("The Message must not be empty")

        else:
            self.print_colored("ERROR, NOT A VALID INPUT", "red")
            

if __name__ == "__main__":
    program = Main()
    program.run()