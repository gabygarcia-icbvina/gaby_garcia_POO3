from .template import CryptoTemplate


class Rot13(CryptoTemplate):
    def __init__(self, message):
        super().__init__(message)
    
    def encode(self):
        original = self.return_original_message()
        resultado = ""
        for caracter in original:

            if 'a' <= caracter <= 'z':
                resultado += chr((ord(caracter) - ord('a') + 13) % 26 + ord('a'))

            elif 'A' <= caracter <= 'Z':
                resultado += chr((ord(caracter) - ord('A') + 13) % 26 + ord('A'))

            else:
                resultado += caracter
        return resultado
