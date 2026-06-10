from .template import CryptoTemplate
from string import ascii_lowercase, ascii_uppercase


class Vigenere(CryptoTemplate):
    def __init__(self, message, key):
        super().__init__(message)
        self.key : str = key
        self.UPPER = list(ascii_uppercase)
        self.LOWER = list(ascii_lowercase)

        if not isinstance(key, str):
            raise TypeError("The Shifts Must be An String Variable!")
    
    def encode(self):
        original = self.return_original_message()
        resultado = []
        self.key = self.key.upper()
        key_idx = 0

        for char in original:

            if char.isalpha():

                shift = ord(self.key[key_idx % len(self.key)]) - ord('A')

                if char.isupper():
                    base = ord('A')
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                else:
                    base = ord('a')
                    new_char = chr((ord(char) - base + shift) % 26 + base)
                    
                resultado.append(new_char)
                key_idx += 1
            else:
                resultado.append(char)
                
        return ''.join(resultado)