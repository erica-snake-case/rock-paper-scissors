import random
SCORING = {"rock": {"beats": "scissors"},
           "scissors": {"beats": "paper"},
           "paper": {"beats": "rock"}}


class InvalidInputError(Exception):
    pass


def beats(symbol1, symbol2):
    """
    returns true if symbol1 beats symbol2
    :param symbol1:
    :param symbol2:
    :return: boolean
    """
    try:
        return SCORING[symbol1]["beats"] == symbol2
    except KeyError:
        raise InvalidInputError(f"must be rock, paper, or scissors, but entered {symbol1}")


def get_result(symbol1, symbol2, player2_name):
    """
    calculates which player wins
    :param symbol1:
    :param symbol2:
    :return: string
    """
    symbol1 = symbol1.lower()
    symbol2 = get_player2_move(player2_name, symbol2.lower())
    if beats(symbol1, symbol2):
        return "player1_wins"
    if beats(symbol2, symbol1):
        return "player2_wins"
    return "ties"


def get_player2_move(name, symbol):
    """
    generates a random move if
    :param symbol1:
    :param symbol2:
    :return: string describing which player wins including ties
    """
    return random.choice(SCORING.keys()) if name == "Computer" else symbol

# TODO:
# save_game(dictionary):
# # append dictionary to csv

# TODO:
# load_game(dictionary):
# read dictionary from csv

# TODO:  move INFORMAL UNIT TESTING to official unit testing
# print("expected = player1_wins")
# print(get_result("scissors", "paper"))

# print("expected = player2_wins")
# print(get_result("rock", "paper"))

# print("expected = ties")
# print(get_result("paper", "paper"))

# print("expected = InvalidInputError")
# print(get_result("scissors", "watermelon"))
# print(get_result("watermelon", "scissors"))
