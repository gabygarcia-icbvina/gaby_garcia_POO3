from .template import CryptoTemplate


class Binary(CryptoTemplate):
    def __init__(self, message):
        super().__init__(message)
    
    def encode(self):
        original = self.return_original_message()
        return ' '.join(format(ord(c), '08b') for c in original)
