class GameState():
    """
    State of a Tic Tac Toe game.
    """
    def __init__(self, playerX, playerO):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def insert_move(self, player, i, j):
        self.assert_valid_move(i, j)
        self.board[i][j] = player

    def assert_valid_move(self, i, j):
        if (i > 2 or i < 0) or (j > 2 or j < 0):
            raise Exception("Your move has out of bounds coordinates.")
        if self.board[i][j] != ' ':
            raise Exception("This move is invalid because it's already played.") # noqa

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


class Game():

    def __init__(self, playerX, playerO):
        # initialize an Game state
        self.state = GameState(playerX, playerO)
        self.playerX = playerX
        self.playerO = playerO
        self.current_player = self.playerX
        self.winner = None

    def start(self):
        """
        Start the game !
        """
        print("To make a move, use the following format: row:column")
        while not self.winner:
            self.state.draw_board()
            self.player_turn()
            self.next_turn()


    def player_turn(self):
        """
        Make the player makes it turn.
        """
        try:
            i, j = self.current_player.make_move(self.state)
            self.state.insert_move(self.current_player, i, j)
            print("Player's move: (%s, %s)" % (i, j))
        except Exception as err:
            print('\n Oops, %s' % err)
            self.wait_for_player_turn()

    def next_turn(self):
        """
        Initiate the next turn.
        """
        if self.current_player is self.playerX:
            self.current_player = self.playerO
        else:
            self.current_player = self.playerX
