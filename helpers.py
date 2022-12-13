SCORING = {"rock": {"beats": "scissors"},
           "scissors": {"beats": "paper"},
           "paper": {"beats": "rock"}}


class InvalidInputError(Exception):
    pass


def beats(symbol1, symbol2):
    try:
        return SCORING[symbol1]["beats"] == symbol2
    except KeyError:
        raise InvalidInputError(f"must be rock, paper, or scissors, but entered {symbol1}")


def get_result(symbol1, symbol2):
    symbol1 = symbol1.lower()
    symbol2 = symbol2.lower()
    if beats(symbol1, symbol2):
        return "player1_wins"
    if beats(symbol2, symbol1):
        return "player2_wins"
    return "ties"

# TODO:
# save_game(dictionary):
# # append dictionary to csv

# INFORMAL UNIT TESTING
# print("expected = player1_wins")
# print(get_result("scissors", "paper"))

# print("expected = player2_wins")
# print(get_result("rock", "paper"))

# print("expected = ties")
# print(get_result("paper", "paper"))

# print("expected = InvalidInputError")
# print(get_result("scissors", "watermelon"))
# print(get_result("watermelon", "scissors"))
