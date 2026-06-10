from .template import CryptoTemplate
import hashlib


class Hash(CryptoTemplate):
    def __init__(self, message):
        super().__init__(message)
    
    def encode(self):
        original = self.return_original_message()
        return hashlib.sha256(original.encode('utf-8')).hexdigest()
