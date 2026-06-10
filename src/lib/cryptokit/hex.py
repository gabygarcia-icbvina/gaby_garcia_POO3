from .template import CryptoTemplate


class Hex(CryptoTemplate):
    def __init__(self, message):
        super().__init__(message)
    
    def encode(self):
        original = self.return_original_message()
        return original.encode('utf-8').hex()
