from abc import ABC, abstractmethod


class CryptoTemplate(ABC):
    def __init__(self, message : str):
        self.__message = message
        if not isinstance(self.__message, str):
            raise TypeError("The Attributes must be its types!")
    
    @abstractmethod
    def encode(self):
        pass
    
    def return_encoded_message(self):
        return self.encode()
    
    def return_original_message(self):
        return self.__message