from game_state import create_board, get_current_player, make_move, check_winner, check_draw


def is_valid_move(board, row, col):
    """Check if move is legal."""
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    return board[row][col] == ' '


def update_game_state(state, row, col):
    """Process a move and return updated state."""
    board = state['board']
    player = get_current_player(state)
    
    if make_move(board, row, col, player):
        state['player'] = player
        return state
    return None


def determine_outcome(state):
    """Returns 'X_win', 'O_win', 'draw', or 'ongoing'."""
    board = state['board']
    winner = check_winner(board)
    
    if winner == 'X':
        return 'X_win'
    elif winner == 'O':
        return 'O_win'
    elif check_draw(board):
        return 'draw'
    return 'ongoing'
