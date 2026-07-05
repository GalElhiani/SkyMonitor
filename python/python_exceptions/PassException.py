#a custom exception module for the password excercise
#Author: Gal Elhiani
#Tester: Meytar

class LengthError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class LowerCaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class UpperCaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class SpecialCharError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class DigitsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
