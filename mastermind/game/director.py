from game.board import Board
from game.console import Console
from game.secret_code import Secret_Code
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self.secret_code = Secret_Code()
        self._roster = Roster()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        self._board._add_names(self._roster.players)
        self._board._to_string
        self.secret_code._create_code()
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the self.current_player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            self.current_player = Player(name)
            self._roster.add_player(self.current_player)
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current self.current_player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        print(f"Current code: {self.secret_code._secret_code}")
        print()
        board = self._board._to_string()
        self._console.write(board)
        # get next player's move
        self.current_player = self._roster.get_current()
        self._console.write(f"{self.current_player.get_name()}'s turn:","player turn")
        self.guess = self._console.read("What is your guess?")
        self.move_result = self.secret_code._check_code(self.guess)
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        
        self._board._update_board(self._roster.current,self.guess,self.move_result)
        self._board._to_string()
        
        
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        
       
        if self.secret_code._check_code(self.guess) == "won":

            self._console.write(self._board._to_string())
            self._console.write(f"{self.current_player.get_name()} won!","victory")
            self._keep_playing = False
        
        self._roster.next_player()


     
       