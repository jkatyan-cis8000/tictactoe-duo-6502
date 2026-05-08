# main.py Design Document

## Overview
Main game loop module orchestrating game flow and coordinating with GameState, GameLogic, and UserInterface modules.

## Implemented Functions

### run_game()
- Initializes empty board and sets starting player to 'X'
- Repeats until win or draw:
  - Displays board
  - Gets player input
  - Validates move
  - Applies move
  - Checks for winner/draw
  - Switches player

### reset_game()
- Returns new empty board and 'X' as starting player
- Tuple: (board, current_player)

### handle_input(board, player)
- Gets player input
- Validates move availability
- Applies move if valid
- Returns True/False for success

## Module Dependencies
- `game_state`: create_board, get_current_player, make_move, check_winner, check_draw
- `game_logic`: is_valid_move, update_game_state, determine_outcome
- `ui`: display_board, get_player_input, display_winner, display_draw, play_again

## Game Flow
1. Initialize board and current player
2. Loop: display → input → validate → move → check → switch
3. On end: display result → ask play again
4. Repeat if requested

## Entry Point
- Runs run_game() directly
- Loops on play_again() response
