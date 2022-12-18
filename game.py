# TODO: Move to database model once postgres implemented
class Game:
    def __init__(self, name1,  name2):
        self.game_id = name1+name2 # TODO: implement better naming system
        self.player1_name = name1 # TODO:  implement  Player class
        self.player1_wins = 0
        self.player2_name = "Computer" if name2 == "" else name2
        self.player2_wins = 0
        self.ties = 0




