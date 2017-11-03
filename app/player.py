class Player():
    """
    Represent a Tic Tac Toe player.
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, state):
        """
        Ask the player to make a move.
        """
        raise NotImplementedError()

    def __str__(self):
        return self.symbol

class HumanPlayer(Player):

    def make_move(self, state):
        play = input("Enter your move: ")
        return self.get_move_coordinates(play)

    def get_move_coordinates(self, move):
        coords = move.split(':')
        if len(coords) < 2:
            raise Exception("Your move is in the wrong format. Use this format --> row:column") # noqa

        i = int(coords[0]) - 1
        j = int(coords[1]) - 1

        return i, j
