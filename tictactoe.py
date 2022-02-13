#Funtion to ask user to choose a letter
def select_letter(player1):
    player1_letter=""
    player2_letter=""
    #Ask user to select a letter (X or O)
    while(player1_letter != "x" and player1_letter != "o"):
        player1_letter=input("Hey "+player1+"!Select X or O: ").replace(" ","").strip().lower()
        #if player 1 chooses "X" ,assign "O" to player 2 and vice versa
        if player1_letter == "x":
            player2_letter="o"
        else:
            player2_letter="x"
    return player1_letter, player2_letter


#Check if board is full
def is_board_full(board):
    return board.count(" ")==0

#Insert a letter (X or O) in a specific position
def insert_letter(board,letter,pos):
    board[pos]=letter

#Print the score board
def print_scoreboard(score_board):
    players = list(score_board.keys())
    print("--------------------------------")
    print("            SCOREBOARD          ")
    print("--------------------------------")
    print('{:<25} {}'.format(players[0], score_board[players[0]]))
    print('{:<25} {}'.format(players[1], score_board[players[1]]))
    print("--------------------------------\n")

#to draw the board
def draw_board(board):
    board[0]=-1
    #draw first row
    print(" _________________")
    print("|     |     |     |")
    print("|  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  |")
    print("|_____|_____|_____|")
    
    #draw second row
    print("|     |     |     |")
    print("|  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  |")
    print("|_____|_____|_____|")
    
    #draw third row
    print("|     |     |     |")
    print("|  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  |")
    print("|_____|_____|_____|")
    
    return board

#Check if a specific player is the winner
def is_winner(board,letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
    (board[4] == letter and board[5] == letter and board[6] == letter) or \
    (board[7] == letter and board[8] == letter and board[9] == letter) or \
    (board[1] == letter and board[4] == letter and board[7] == letter) or \
    (board[2] == letter and board[5] == letter and board[8] == letter) or \
    (board[3] == letter and board[6] == letter and board[9] == letter) or \
    (board[1] == letter and board[5] == letter and board[9] == letter) or \
    (board[3] == letter and board[5] == letter and board[7] == letter)

#Repeat the game
def repeat_game():
    
    repeat=input("Play again? Press y for yes and n for no: ")
    while repeat != "n" and repeat != "y":
        repeat=input("PLEASE, press y for yes and n for no: ")
    return repeat

#Take player input
def player_input(curr_player,board,letter):
    while True:
        try:
            position=int(input(curr_player+",select a position (1-9) to place an "+letter+" : " ))
        except:
            continue
        else:
            break
            
    while True:
        #check if user selects out of range position
        if (position not in range(1,10)) or (board[position] != " "):
            position=int(input(curr_player+",please, choose another position to place an "+letter+" from 1 to 9 :"))
        else:
            break
    insert_letter(board,letter,position) #insert the letter(X or O) in the position on the board
    
#Play the game
def play_game(board,player1,player2,score_board):
    curr_player=player1
    player1_letter, player2_letter= select_letter(player1)
    #clean the board
    board=[" " for i in range(10)] #create an array to store the values in the board
    board=draw_board(board)
    #check if there are empty positions on the board
    while is_board_full(board) == False:
        if curr_player==player1:
            player_input(player1,board,player1_letter)
            curr_player=player2
        else:
            player_input(player2,board,player2_letter)
            curr_player=player1
        #draw the board
        board=draw_board(board)

        #check if player 1 is winner
        if is_winner(board,player1_letter):
            print("\n Congratulations!"+player1+" Won.")
            score_board[player1] = score_board[player1] + 1
            print_scoreboard(score_board)
            return repeat_game()
        #check if player 2 is winner
        elif is_winner(board,player2_letter):
            score_board[player2] = score_board[player2] + 1
            print("\n Congratulations!"+player2+" Won.")
            print_scoreboard(score_board)
            return repeat_game()

    #if " " not in board:
    if is_board_full(board):
        print("\n Its a Draw :(")
        print_scoreboard(score_board)
        return repeat_game()

#Start the game
print("Let play Tic Tac Toe")
repeat="y"
board=[" " for i in range(10)] #create an array to store the values in the board
board=draw_board(board)
while True:
    player1=input("Enter player 1 name: ")
    player2=input("Enter player 2 name: ")
    if player1=='' or player2=='' or (not player1.isalpha()) or (not player2.isalpha()) : #check if layer name is '' or is not alphabetic
        print("Come On! You definitely have a name.Even nickname will be cool ;).")
    else:
        if player1==player2:
            print("Hey! Give some unique names!")
        else:
            break

score_board={player1:0,player2:0} #initialize scoreboard
print_scoreboard(score_board)
while(repeat.lower()=="y"):
    repeat=play_game(board,player1,player2,score_board)