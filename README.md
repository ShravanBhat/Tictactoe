# Tictactoe

### Assumptions
- Board will be standard 3x3

### Files
- tictacoe_2 player.py is 1.0 Release. It is a multiplayer game.<br/>
- tictactoe_final.py is final Release.One can play with computer as well as with a human.
- tests_all_unit.py -Used for testing purposes

### How to play
- Clone the repo<br/>
- Open the terminal<br/>
- python tictactoe_final.py 

### Explanation of Funtions in the above programs
- tictactoe_2 player.py
```
main() : Takes player names
play_game() : Main funtion which runs the flow of the game
choose_letter() : Takes input of letter choice(X or O) from Player 1 and assigns the other letter to player 2
draw_grid() : Prints the grid
player_input() : Takes the player input for the position to place X or O
is_winner() : Checks if the particular player won or not
is_grid_full() : Checks if the grid has ay empty space or not.If grid is full then no one has won till now and its a draw
print_scoreboard() : Prints the scoreboard containing player names and their respective scores
repeat_game() : Repeat the game until user presses N
```
- tictactoe_final.py
```
main() : Take extra input of game_type. 1 means single player and 2 means 2 player
If 2 is selected multiplayer logic as mentioned in 'tictactoe_2 player.py' is run
If 1 is selected, second player will be computer
play_game() : Main funtion which runs the flow of the game
choose_letter() : Takes input of letter choice(X or O) from Player 1 and assigns the other letter to player 2
draw_grid() : Prints the grid
player_input() : Takes the player input for the position to place X or O
computer() : This function contains the logic for computer moves
Computer checks if it can make a winning move or prevent the opponent from making winning move by placing its letter in any of the empty position.
If it cant win or prevent opponent from winning: 
1)It checks for empty corners to place the letter and randomly places letter in any empty corner
2)If no corners are empty it places letter in middle position if its empty
3)If even mid is occupied it checks for any remaining slot and randomly places its letter on the available empty slot
is_winner() : Checks if the particular player won or not
is_grid_full() : Checks if the grid has ay empty space or not.If grid is full then no one has won till now and its a draw
print_scoreboard() : Prints the scoreboard containing player names and their respective scores
repeat_game() : Repeat the game until user presses N
```
