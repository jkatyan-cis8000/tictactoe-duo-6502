from game_state import create_board, get_current_player, make_move, check_winner, check_draw
from game_logic import is_valid_move, update_game_state, determine_outcome
from ui import display_board, get_player_input, display_winner, display_draw, play_again


def run_game():
    """Main game loop."""
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        row, col = get_player_input(current_player)
        
        if not is_valid_move(board, row, col):
            print("Spot already taken. Try again.")
            continue
        
        make_move(board, row, col, current_player)
        outcome = determine_outcome({'board': board, 'current_player': current_player})
        
        if outcome == 'X_win':
            display_winner('X')
            break
        elif outcome == 'O_win':
            display_winner('O')
            break
        elif outcome == 'draw':
            display_draw()
            break
        
        current_player = 'O' if current_player == 'X' else 'X'


def reset_game():
    """Initialize new game state."""
    return create_board(), 'X'


def handle_input(board, player):
    """Validate and apply player move."""
    row, col = get_player_input(player)
    if is_valid_move(board, row, col):
        make_move(board, row, col, player)
        return True
    return False


if __name__ == "__main__":
    run_game()
    while play_again():
        run_game()
