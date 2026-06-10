from .template import CryptoTemplate
from string import ascii_lowercase, ascii_uppercase


class Caesar(CryptoTemplate):
    def __init__(self, message, shifts):
        super().__init__(message)
        self.shifts = shifts
        self.UPPER = list(ascii_uppercase)
        self.LOWER = list(ascii_lowercase)

        if not isinstance(shifts, int):
            raise TypeError("The Shifts Must be An Integer Variable!")
    
    def encode(self):
        original = self.return_original_message()
        encoded_chars = []
        shift = self.shifts % 26

        for char in original:
            if char.isupper():
                index = self.UPPER.index(char)
                encoded_chars.append(self.UPPER[(index + shift) % 26])
            elif char.islower():
                index = self.LOWER.index(char)
                encoded_chars.append(self.LOWER[(index + shift) % 26])
            else:
                encoded_chars.append(char)

        return "".join(encoded_chars)
