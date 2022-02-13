def draw_board(board):
    board[0]=-1
    #draw first row
    print("    |     |    ")
    print("  "+board[1]+" |  "+board[2]+"  | "+board[3]+" ")
    print("____|_____|____")
    
    #draw second row
    print("    |     |    ")
    print(" "+board[4]+"  |  "+board[5]+"  | "+board[6]+" ")
    print("____|_____|____")
    
    #draw third row
    print("    |     |    ")
    print(" "+board[7]+"  |  "+board[8]+"  |  "+board[9]+" ")
    print("    |     |    ")
    
    return board
def is_winner(board,letter):
    return  (board[1] == letter and board[2] == letter and board[3] == letter) or \
            (board[4] == letter and board[5] == letter and board[6] == letter) or \
            (board[7] == letter and board[8] == letter and board[9] == letter) or \
            (board[1] == letter and board[4] == letter and board[7] == letter) or \
            (board[2] == letter and board[5] == letter and board[8] == letter) or \
            (board[3] == letter and board[6] == letter and board[9] == letter) or \
            (board[1] == letter and board[5] == letter and board[9] == letter) or \
            (board[3] == letter and board[5] == letter and board[7] == letter)
def play_game():
    # Represents the Tic Tac Toe
    board = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        draw_board(board)
         
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Check if the box is not occupied already
        if board[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Update game information
 
        # Updating grid status 
        board[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if is_winner(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

def start_game(player1,player2):
    score_board={player1:0,player2:0}
    print_scoreboard(score_board)
    current_player=player1 #store current player name
    player_choice={'X':"",'O':""} #store player choices
    options = ['X', 'O']

    while True:
        print("Turn to choose for", current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
        try:
            choice = int(input())   
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
            
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break  

        else:
            print("Wrong Choice!!!! Try Again\n")

        # Stores the winner in a single game of Tic Tac Toe
        winner = play_game(options[choice-1])
            
        # Edits the scoreboard according to the winner
        if winner != 'Draw' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t            SCOREBOARD          ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")


print("Tic Tac Toe")
while True:
    game_type=input("Enter The game type.1 for computer 2 for 2 player")
    if game_type=='1' or game_type=='2':
        game_type=int(game_type)
        break
    else:
        game_type=input("Please enter 1 for computer 2 for 2 player")
    
    
if game_type==1:
    player1=input("Enter player name")
    player2="Computer"
else:
    player1=input("Enter player 1 name")
    player2=input("Enter player 2 name")
start_game(player1,player2)