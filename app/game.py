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
        play = input("Enter your move: ")
        print("Player's move: %s" % play)
