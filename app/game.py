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

        moves = 0
        while not self.winner and moves < 9:
            self.state.draw_board()
            self.player_turn()
            if self.is_winning():
                self.winner = self.current_player
            self.next_turn()
            moves += 1

        if moves == 9 and not self.winner:
            self.draw()
        else:
            self.show_winner()

    def player_turn(self):
        """
        Make the player makes it turn.
        """
        try:
            print("Player '%s' is playing" % self.current_player)
            i, j = self.current_player.make_move(self.state)
            self.state.insert_move(self.current_player, i, j)
        except Exception as err:
            print('\n Oops, %s' % err)
            self.player_turn()

    def next_turn(self):
        """
        Initiate the next turn.
        """
        if self.current_player is self.playerX:
            self.current_player = self.playerO
        else:
            self.current_player = self.playerX

    def is_winning(self):
        for i in range(3):
            board = self.state.board
            h = board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' '
            v = board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' '

            if h or v:
                return True

    def draw(self):
        print("""
                ____
  __/|___/|_   / __ \_________ __      __   __/|___/|_
 |    /    /  / / / / ___/ __ `/ | /| / /  |    /    /
/_ __/_ __|  / /_/ / /  / /_/ /| |/ |/ /  /_ __/_ __|
 |/   |/    /_____/_/   \__,_/ |__/|__/    |/   |/

        """)

    def show_winner(self):
        print("""
                _________    __  _________   ____ _    ____________
  __/|___/|_   / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \   __/|___/|_
 |    /    /  / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /  |    /    /
/_ __/_ __|  / /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/  /_ __/_ __|
 |/   |/     \____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|    |/   |/

        """)
        self.state.draw_board()
        print("WINNER IS : %s" % self.winner)
