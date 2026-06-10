from typing import Literal
from .cryptokit import caesar, vigenere, hash, rot13, hex, binary
from termcolor import colored


class CryptoMania:
    encode_methods = Literal["Caesar", "Vigenere", "Hash", "Rot13", "Hex", "Binary"]
    def __init__(self, encode_method : encode_methods, message : str, shifts : int | None = None, key : str | None = None):
        self.encode_method = encode_method
        self.__message = message
        self.shifts = shifts
        self.key = key

    def run(self):
        if self.encode_method == "Caesar":
            if not self.shifts:
                raise CryptoManiaEncodeMethodError("You must enter a shift for this encode")
            elif not isinstance(self.shifts, int):
                raise TypeError("The type of shifts must be an integer")
            else:
                self.__message = caesar.Caesar(self.__message, self.shifts).encode()
        
        elif self.encode_method == "Vigenere":
            if not self.key:
                raise CryptoManiaEncodeMethodError("You must enter a key for this encode")
            elif not isinstance(self.key, str):
                raise TypeError("The type of key must be an string")
            else:
                self.__message = vigenere.Vigenere(self.__message, self.key).encode()

        elif self.encode_method == "Hash":
            self.__message = hash.Hash(self.__message).encode()
        
        elif self.encode_method == "Rot13":
            self.__message = rot13.Rot13(self.__message).encode()
            
        elif self.encode_method == "Hex":
            self.__message = hex.Hex(self.__message).encode()

        elif self.encode_method == "Binary":
            self.__message = binary.Binary(self.__message).encode()
            
        else: raise CryptoManiaEncodeMethodError("Invalid Encode Method.")

        return self
    
    def printMessage(self):
        print(colored(f"Message : '{self.__message}'", "light_green"))

class CryptoManiaEncodeMethodError(Exception):
    pass