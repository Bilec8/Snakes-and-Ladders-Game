# Snakes and Ladders Game

## Overview
This is a Python implementation of the classic **Snakes and Ladders** board game. The game allows multiple players to roll dice, move across the board, and interact with snakes and ladders as they race to reach the final square (square 100). The game supports multiple players and features the logic for snake and ladder interactions.

## Rules
- Each player rolls a dice.
- The player moves the number of steps equal to the dice roll. If a player rolls a 6, they roll again and add the new roll to their total.
- If a player lands on a square with a ladder, they move to the top of the ladder. Ladders move only upwards.
- If a player lands on a square with a snake, they move to the tail of the snake.
- If a player lands on a square where another player's piece is located, that player’s piece is moved one square back. The same rules for ladders, snakes, and collisions apply to this piece.
- The first player to land on square 100 wins the game. Players must land exactly on square 100—if they roll too high, the move is invalid and does not take place.

## Requirements
- Python 3.x
- No external libraries required

## How to Play
1. Run the script to start the game.
2. The game will prompt for the number of players and each player's name.
3. Players take turns rolling a dice. They will be notified of their moves and the game board state.
4. The game continues until one player reaches square 100 exactly.

## Setup and Running the Game
1. First, clone the repository with the following command:

```bash
git clone https://github.com/Bilec8/Snakes-and-Ladders-Game.git
```

2. Navigate to the directory containing the game script:

```bash
cd Snakes-and-Ladders-Game
```

3. Now, simply run the game with this command:

```bash
py main.py
```
