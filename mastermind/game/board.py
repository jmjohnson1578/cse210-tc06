import colorama

class Board:
    """The board displayed after each guess, with code hints. 
    The responsibility of board is to keep track of the player's last guesses and hints

    Stereotype:
        Information Holder

    Attributes:
        _player_names (list): a list of player names
        _player_guesses (list): a list of strings of player's last guesses
        _player_hints (list): a list of strings of player's last hints
    """
    def __init__(self):
        self._player_names = []
        self._player_colors = [colorama.Fore.GREEN,colorama.Fore.RED]

        self.board_color = colorama.Fore.CYAN

        self._player_guesses = ["----","----"]
        self._player_hints = ["****","****"]
        self.current_board = ""
    
    def _add_names(self,names):
        for name in names:
            self._player_names.append(name.get_name())

    def _to_string(self):
        self.current_board =f"{self.board_color}" +  "-" * 10 
        for n in range(0,len(self._player_guesses)):
            
            self.current_board += f"\n{self._player_colors[n]}{self._player_names[n]}: {self._player_guesses[n]}, {self._player_hints[n]}"
        
        self.current_board += f"{self.board_color}\n" + ("-" * 10)
        return self.current_board
    
    def _update_board(self,player_num,guess,result):
        self._player_guesses[player_num] = guess
        self._player_hints[player_num] = result
        



    