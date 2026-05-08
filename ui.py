def display_board(board):
    """Print formatted 3x3 grid."""
    print("\n   1   2   3")
    for i, row in enumerate(board):
        print(f"{i + 1}  {row[0] or ' '} | {row[1] or ' '} | {row[2] or ' '}")
        if i < 2:
            print("  ---|---|---")
    print()


def get_player_input(player):
    """Prompt for row and column (1-3)."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1
            if row in (0, 1, 2) and col in (0, 1, 2):
                return row, col
            print("Invalid input. Enter numbers 1-3.")
        except ValueError:
            print("Invalid input. Enter numbers 1-3.")


def display_winner(winner):
    """Show winning message."""
    print(f"\nPlayer {winner} wins!")


def display_draw():
    """Show draw message."""
    print("\nIt's a draw!")


def play_again():
    """Ask if players want new game."""
    return input("Play again? (y/n): ").lower().startswith('y')
