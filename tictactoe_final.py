import random
#Funtion to ask user to choose a letter
def choose_letter(player1):
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
def is_grid_full(grid):
    return grid.count(" ")==0

#Insert a letter (X or O) in a specific position
def insert_letter(grid,letter,pos):
    grid[pos]=letter

#Print the score board
def print_scoreboard(score_board):
    players = list(score_board.keys())
    print("--------------------------------")
    print("            SCOREBOARD          ")
    print("--------------------------------")
    print('{:<25} {}'.format(players[0], score_board[players[0]]))
    print('{:<25} {}'.format(players[1], score_board[players[1]]))
    print("--------------------------------\n")

#to draw the grid
def draw_grid(grid):
    grid[0]=-1
    #draw first row
    print(" _________________")
    print("|     |     |     |")
    print("|  "+grid[1]+"  |  "+grid[2]+"  |  "+grid[3]+"  |")
    print("|_____|_____|_____|")
    
    #draw second row
    print("|     |     |     |")
    print("|  "+grid[4]+"  |  "+grid[5]+"  |  "+grid[6]+"  |")
    print("|_____|_____|_____|")
    
    #draw third row
    print("|     |     |     |")
    print("|  "+grid[7]+"  |  "+grid[8]+"  |  "+grid[9]+"  |")
    print("|_____|_____|_____|")
    
    return grid

#Computer moves
def computer(grid,computer_letter):
    possible_moves=[]
    available_corners=[]
    available_center=[]
    available_edges=[]
    position=-1

    #Append all the possible moves
    for i in range(1,len(grid)):
        if grid[i] ==" ":
            possible_moves.append(i)

    #if the position can make X or O wins!
    #The computer will choose it to win or ruin a winning of the user
    for lettr in ["x","o"]:
        for i in possible_moves:
            grid_copy=grid[:]
            grid_copy[i] = lettr
            if is_winner(grid_copy,lettr):
                position=i


    #If the computer can't win or ruin a winning,it will choose a random position starting with the corners, the center then the edges
    if position == -1:
        for i in range(len(grid)):
            #an empty index on the grid
            if grid[i]==" ":
                if i in [1,3,7,9]:
                    available_corners.append(i)
                if i== 5:
                    available_center.append(i)
                if i in [2,4,6,8]:
                    available_edges.append(i)
        #Check the corners first
        if len(available_corners)>0:
            #Select a random position
            position=random.choice(available_corners)
        #Then check the availability of the center
        elif len(available_center)>0:
            position=available_center[0]
        #Check the edges
        elif len(available_edges)>0:
            #select a random position
            position=random.choice(available_edges)
    #fill the position with the letter
    insert_letter(grid,computer_letter,position)

#Check if a specific player is the winner
def is_winner(grid,letter):
    return (grid[1] == letter and grid[2] == letter and grid[3] == letter) or \
    (grid[4] == letter and grid[5] == letter and grid[6] == letter) or \
    (grid[7] == letter and grid[8] == letter and grid[9] == letter) or \
    (grid[1] == letter and grid[4] == letter and grid[7] == letter) or \
    (grid[2] == letter and grid[5] == letter and grid[8] == letter) or \
    (grid[3] == letter and grid[6] == letter and grid[9] == letter) or \
    (grid[1] == letter and grid[5] == letter and grid[9] == letter) or \
    (grid[3] == letter and grid[5] == letter and grid[7] == letter)

#Repeat the game
def repeat_game():
    
    repeat=input("Play again? Press y for yes and n for no: ")
    while repeat.lower() != "n" and repeat.lower() != "y":
        repeat=input("PLEASE, press y for yes and n for no: ")
    return repeat

#Take player input
def player_input(curr_player,grid,letter):
    while True:
        try:
            position=int(input(curr_player+",select a position (1-9) to place an "+letter+" : " ))
        except:
            continue
        else:
            break
            
    while True:
        #check if user selects out of range position
        try:
            if (position not in range(1,10)) or (grid[position] != " "):
                position=int(input(curr_player+",please, choose another position to place an "+letter+" from 1 to 9 :"))
        except:
            continue
        else:
            break
    insert_letter(grid,letter,position) #insert the letter(X or O) in the position on the grid
    
#Play the game
def play_game(game_type,grid,player1,player2,score_board):
    curr_player=player1
    player1_letter, player2_letter= choose_letter(player1)
    #clean the grid
    grid=[" " for i in range(10)] #create an array to store the values in the grid
    grid=draw_grid(grid)
    #check if there are empty positions on the grid
    while is_grid_full(grid) == False:

        if game_type==2:
            if curr_player==player1:
                player_input(player1,grid,player1_letter)
                curr_player=player2
            else:
                player_input(player2,grid,player2_letter)
                curr_player=player1
        else:
            player_input(player1,grid,player1_letter)
            print("\n Computer's Turn:")
            grid=draw_grid(grid)
            computer(grid,player2_letter)
        #draw the grid
        grid=draw_grid(grid)

        #check if player 1 is winner
        if is_winner(grid,player1_letter):
            print("\n Congratulations! "+player1.upper()+" Won.")
            score_board[player1] = score_board[player1] + 1
            print_scoreboard(score_board)
            return repeat_game()
        #check if player 2 is winner
        elif is_winner(grid,player2_letter):
            if game_type==1:
                print("Hard Luck! Computer won")
            else:
                print("\n Congratulations! "+player2.upper()+" Won.")
            score_board[player2] = score_board[player2] + 1
            print_scoreboard(score_board)
            return repeat_game()

    #if " " not in grid:
    if is_grid_full(grid):
        print("\n Its a Draw :(")
        print_scoreboard(score_board)
        return repeat_game()

#Start the game
if __name__=="__main__":
    print("Lets play Tic Tac Toe")
    repeat="y"
    grid=[" " for i in range(10)] #create an array to store the values in the grid
    grid=draw_grid(grid)
    while True:
        game_type=input("Enter:\n 1 to play vs Computer \n 2 to play with a human : ")
        if game_type=='1' or game_type=='2':
            game_type=int(game_type)
            break
        else:
            game_type=input("Please enter 1 for computer 2 for 2 player")
    while True:
        if game_type==1:
            player1=input("Enter Player's name: ")
            player2="Computer"
            if player1!='':
                break
        else:
           #2 player
            player1=input("Enter Player 1 name: ")
            player2=input("Enter Player 2 name: ")
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
        repeat=play_game(game_type,grid,player1,player2,score_board)