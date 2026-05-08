# ui.py Design Document

## Overview
User interface module handling display of game state and collection of player input.

## Implemented Functions

### display_board(board)
- Renders the 3x3 grid in formatted output
- Shows column headers (1-3) and row numbers (1-3)
- Displays empty cells as spaces

### get_player_input(player)
- Prompts current player for row and column
- Validates input is numeric and in range 1-3
- Returns zero-indexed (row, col) tuple

### display_winner(winner)
- Announces winning player

### display_draw()
- Announces draw condition

### play_again()
- Asks players if they want to restart
- Returns True for 'y' or 'Y' input

## Constraints
- Uses standard library only (print, input)
- Input validation prevents out-of-bounds errors
- Zero-indexed coordinates internally, 1-3 displayed to users
