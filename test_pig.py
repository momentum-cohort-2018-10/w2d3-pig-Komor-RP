from pig import Dice, Player, Game, ComputerPlayer

dice = Dice()
player1 = Player()
player2 = ComputerPlayer()

def test_dice_exists():
    new_dice = Dice()
    assert type(new_dice) == Dice

def test_dice_equality():
    dice1 = Dice()
    dice2 = Dice()
    assert dice1 == dice2 

def test_dice_will_roll_within_params():
    for _ in range(15):
        assert dice.roll() in range(1,7)

def test_player_exists():
    new_player = Player()
    assert type(new_player) == Player
    assert new_player.score == 0

def test_score_add():
    new_player = Player()
    new_cpu = ComputerPlayer()
    new_player.add_points(20)
    new_cpu.add_points(25)
    assert new_player.score == 20
    assert new_cpu.score == 25


def test_computer_exists():
    new_computer = ComputerPlayer()
    assert type(new_computer) == ComputerPlayer
    assert new_computer.score == 0

def test_computer_decide_die_roll():
    new_computer = ComputerPlayer()
    assert new_computer.decide_roll_die(20) == False
    assert new_computer.decide_roll_die(5) == True

def test_get_first_player():
    new_game = Game()
    assert new_game.choose_first_player() == new_game.player1 or new_game.cpu



