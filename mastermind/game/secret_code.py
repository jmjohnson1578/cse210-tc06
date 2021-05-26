import random
class Secret_Code:
    """Class to create and store a random 4-digit secret code for each round and return hints and check for win
    
    Stereotype:
        Information Holder

    Attributes:
    _secret_code (string): a string containing a super-secret random 4-digit code

    """
    def __init__(self):
        self._secret_code = ""

    @property
    def secret_code(self):
        return self._secret_code

    def _create_code(self):
        for _ in range(4):
            digit = random.randint(0,9)
            self._secret_code += str(digit)

        
    def _check_code(self,code):
        #Check first up to see if the code guessed is correct
        guess_return = ""
        if code == self._secret_code:
            return "won"
        else:
            for digit in range(4):
                if code[digit] == self._secret_code[digit]:
                    guess_return += "x"
                elif code[digit] in self._secret_code:
                    guess_return += "o"
                else:
                    guess_return += "*"
        
        return guess_return
            
