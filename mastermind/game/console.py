import random
import colorama

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
        
    """
    def __init__(self):
        self.input_color = colorama.Fore.YELLOW
        self.victory_color = colorama.Fore.MAGENTA

    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(f"{self.input_color}{prompt}")

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            integer: The user's input as an integer.
        """
        return int(input(prompt))
        
    def write(self, text,text_type=None):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        if text_type == "victory":
            print(f"{self.victory_color}{text}")
        elif text_type == "player turn":
            print(f"{self.input_color}{text}")
        else:
            print(text)