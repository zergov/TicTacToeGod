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


class GodMove():
    def __init__(self, i, j, score):
        self.i = i
        self.j = j
        self.score = score


class GodPlayer(Player):

    def make_move(self, state):
        return self.find_best_move(state.board)

    def evaluate_board(self, board):
        """
        Check if player is winning, and return a score based on the outcome.
        10 if winning
        -10 if losing
        0 if draw
        """
        # Check for vertical / horizontal terminated case
        for i in range(3):
            h = board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' '
            v = board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' '

            if h or v:
                return 10 if board[i][0] == self.symbol else -10
        # Diagonal check
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
                return 10 if board[0][0] == self.symbol else -10
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
                return 10 if board[0][2] == self.symbol else -10

        return 0

    def has_more_move(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return True
        return False

    def minimax(self, board, is_max):
        score = self.evaluate_board(board)

        if score == 10:
            return score

        if score == -10:
            return score

        if not self.has_more_move(board):
            return 0

        if is_max:  # if bot is playing
            best = -100000

            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = self.symbol
                        best = max(best, self.minimax(board, False))
                        board[i][j] = ' '
            return best
        else:       # if human is playing
            best = 100000

            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        best = min(best, self.minimax(board, True))
                        board[i][j] = ' '
            return best

    def find_best_move(self, board):
        best_score = -100000
        move_i = -1
        move_j = -1

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':

                    board[i][j] = self.symbol  # make the move
                    score = self.minimax(board, False)
                    board[i][j] = ' '  # revert the move

                    if score > best_score:
                        best_score = score
                        move_i = i
                        move_j = j

        return move_i, move_j
