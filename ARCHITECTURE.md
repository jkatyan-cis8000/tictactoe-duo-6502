# Tic-Tac-Toe Game Architecture

## Overview
A minimalist two-player Tic-Tac-Toe game with a user-friendly interface. Players alternate placing X or O on a 3x3 grid until someone wins or the board fills.

## Modules

### 1. GameState (`game_state.py`)
**Responsibility:** Track the current state of the board, player turns, and game progress.

**Interfaces:**
- `create_board()` - Initialize empty 3x3 grid
- `get_current_player(state)` - Returns 'X' or 'O' based on turn
- `make_move(board, row, col, player)` - Place player's mark if spot is empty
- `check_winner(board)` - Returns winning player or None
- `check_draw(board)` - Returns True if board is full with no winner
- `get_winning_combinations()` - Returns list of winning row/col/diagonal tuples

### 2. GameLogic (`game_logic.py`)
**Responsibility:** Core game rules and validation.

**Interfaces:**
- `is_valid_move(board, row, col)` - Check if move is legal
- `update_game_state(state, row, col)` - Process a move and return updated state
- `determine_outcome(state)` - Returns 'X_win', 'O_win', 'draw', or 'ongoing'

### 3. UserInterface (`ui.py`)
**Responsibility:** Display the game and collect player input.

**Interfaces:**
- `display_board(board)` - Print formatted grid
- `get_player_input(player)` - Prompt for row and column (1-3)
- `display_winner(winner)` - Show winning message
- `display_draw()` - Show draw message
- `play_again()` - Ask if players want new game

### 4. MainGame (`main.py`)
**Responsibility:** Orchestrate game flow, tie modules together.

**Interfaces:**
- `run_game()` - Main game loop
- `reset_game()` - Initialize new game state
- `handle_input(board, player)` - Validate and apply player move

## File Assignments
- **Teammate 1:** `game_state.py` + `game_logic.py`
- **Teammate 2:** `ui.py` + `main.py`

## Data Flow
1. MainGame initializes GameState
2. UserInterface displays board and collects input
3. GameLogic validates and processes moves
4. GameState tracks board state and checks win conditions
5. Loop continues until game ends
