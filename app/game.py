class Game():

    def __init__(self):

        # initialize an empty board
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

        self.draw_board()

    def draw_board(self):
        """
        Draw the board on the console.
        """
        print('-' * 7)
        for i in range(3):
            output = ''
            for j in range(3):
                if not j:
                    output += '|'
                output += '%s|' % self.board[i][j]
            print(output)
            print('-' * 7)

    def wait_for_player_turn(self):
        """
        Wait for the player's turn.
        """
