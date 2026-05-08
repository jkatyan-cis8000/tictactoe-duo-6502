BOARD_SIZE = 3


def create_board():
    """Initialize empty 3x3 grid."""
    return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def get_current_player(state):
    """Returns 'X' or 'O' based on turn."""
    if state.get('player') is None:
        return 'X'
    return 'O' if state['player'] == 'X' else 'X'


def make_move(board, row, col, player):
    """Place player's mark if spot is empty."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def check_winner(board):
    """Returns winning player or None."""
    winning_combinations = get_winning_combinations()
    for combo in winning_combinations:
        cells = [board[r][c] for r, c in combo]
        if cells[0] != ' ' and cells.count(cells[0]) == len(cells):
            return cells[0]
    return None


def check_draw(board):
    """Returns True if board is full with no winner."""
    for row in board:
        if ' ' in row:
            return False
    return True


def get_winning_combinations():
    """Returns list of winning row/col/diagonal tuples."""
    combinations = []
    for i in range(BOARD_SIZE):
        combinations.append([(i, j) for j in range(BOARD_SIZE)])
        combinations.append([(j, i) for j in range(BOARD_SIZE)])
    combinations.append([(i, i) for i in range(BOARD_SIZE)])
    combinations.append([(i, BOARD_SIZE - 1 - i) for i in range(BOARD_SIZE)])
    return combinations
