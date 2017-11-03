class Game():

    def __init__(self):
        # initialize an empty board
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

        self.winner = None

    def start(self):
        """
        Start the game !
        """
        print("To make a move, use the following format: row:column")
        while not self.winner:
            self.draw_board()
            self.wait_for_player_turn()

    def draw_board(self):
        """
        Draw the board on the console.
        """
        print('\n   1 2 3')
        print('  ' + ('-' * 7))
        for i in range(3):
            output = ''
            for j in range(3):
                if not j:
                    output += '%s |' % (i + 1)
                output += '%s|' % self.board[i][j]
            print(output)
            print('  ' + ('-' * 7))
        print()

    def wait_for_player_turn(self):
        """
        Wait for the player's turn.
        """
        try:
            play = input("Enter your move: ")
            i, j = self.get_move_coordinates(play)
            self.board[i - 1][j - 1] = 'X'
            print("Player's move: %s" % play)
        except Exception as err:
            print('\n Oops, %s' % err)
            self.wait_for_player_turn()

    def get_move_coordinates(self, move):
        coords = move.split(':')
        if len(coords) < 2:
            raise Exception("Your move is in the wrong format. Use this format --> row:column") # noqa

        i = int(coords[0])
        j = int(coords[1])

        if (i > 3 or i < 1) or (j > 3 or j < 1):
            raise Exception("Your move has out of bounds coordinates.")

        if self.board[i - 1][j - 1] != ' ':
            raise Exception("This move is invalid because it's already played.") # noqa

        return i, j
