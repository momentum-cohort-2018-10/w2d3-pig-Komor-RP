import random

class Dice:
    def __init__(self):
        """
        Dice with no attributes.
        """
        pass

    def __eq__(self, other):
        "Equality method for Dice"
        return type(self) == type(other)

    def roll(self):
        """
        Gets a random number from 1,6 inclusive.
        """
        result = random.randint(1, 6)
        print(f'Roll Result: {result}')
        return result



class Player:
    def __init__(self, name):
        """
        Player with a name to refer to, and a score.
        """
        self.name = name
        self.score = 0

    def __eq__(self, other):
        """
        Equality method for Player compares type, score, and name.
        """
        return type(self) == type(other) and self.score == other.score and self.name == other.name

    def __str__(self):
        """
        Returns player name.
        """
        return self.name

    def decide_roll_die(self, points) -> bool:
        """
        Asks for input in whether to roll a die.
        """
        choice = input(f"You currently have {points} points this turn. Will you roll the die? (y) or (n) ")
        return choice == "y"

    def add_points(self, points):
        """
        Adds to the player's score.
        """
        self.score += points

class ComputerPlayer(Player):
    """
    Player child
    """
    def decide_roll_die(self, points) -> bool:
        """
        Computer Player has it's own decide_roll_die that returns True 
        if points is less than 20, meaning it will roll.
        """
        print(f"{self.name} currently has {points} points this turn.")
        if points < 20:
            print(f"{self.name} rolls the die.")
            return True
        print(f"{self.name} holds.")



class Game:
    wins = 0
    games = 0

    def __init__(self):
        """
        Parameters:
        - dice - game Dice object
        - player1 - Player object that asks for input
        - cpu - ComputerPlayer object that is set to play a certain way
        - first_player - keeps track of first_player in order to alternate between games
        - turn - keeps track of whose turn it is
        - status - will change once there is a winner
        """

        self.dice = Dice()
        self.player1 = Player("Player 1")
        self.cpu = ComputerPlayer("CPU")
        self.first_player = None
        self.turn = None
        self.status = None
        

    def choose_first_player(self):
        """
        Randomly chooses a player and makes it their turn
        """
        self.turn = random.choice([self.player1, self.cpu]) 
        self.first_player = self.turn

    def display_scores(self):
        """
        Updates the terminal with both player scores.
        """
        print(f'Your Score: {self.player1.score} \nOpponent Score: {self.cpu.score}')

    def run_game(self):
        """
        Runs the entire game.
        """
        if Game.games == 0:
            self.choose_first_player()

        print(f'First player to go is {str(self.turn)}.')

        while not self.status:
            self.play_round()

        print(f"Your win ratio is {Game.wins}/{Game.games}")
        replay = input("Do You Want To Play Again? (y) or (n) ")
        if replay == 'y':
            self.reset_game()
            self.run_game()


    def check_winner(self, points):
        """
        Checks the player scores to see if anyone has won.
        Changes the Game status and updates Game games and Game wins
        """
        if self.turn.score + points >= 20:
            print(f"{self.turn} is the winner!")

            Game.games += 1
            if self.turn == self.player1:
                Game.wins += 1

            return True

    def play_round(self):
        """
        A single round of the game where a player takes their turn and rolls
        the die until they hold or roll a 1.
        """
        print("-" * 30)

        points = 0

        self.display_scores()
        print(f"It is {self.turn}'s turn")

        roll = 2
        while(self.turn.decide_roll_die(points) and roll > 1):
            roll = self.dice.roll()
            points += roll
            if roll == 1:
                points = 0
                break
            
            self.status = self.check_winner(points)
            if self.status is not None:
                break

        input("Press enter to continue.")
        self.turn.add_points(points)

        

        self.switch_turns()

    def switch_turns(self):
        """
        Toggles the turns
        """
        if (self.turn == self.cpu):
            self.turn = self.player1
        else:
            self.turn = self.cpu

    def reset_game(self):
        """
        Sets variables so they'll be ready for a replay.
        """ 
        if self.first_player == self.player1:
            self.first_player = self.cpu
            self.turn = self.cpu
        else:
            self.first_player = self.player1
            self.turn = self.player1

        self.dice = Dice()
        self.player1.score = 0
        self.cpu.score = 0
        self.status = None

    


new_game = Game()
new_game.run_game()
