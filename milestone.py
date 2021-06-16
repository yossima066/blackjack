

# Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print( board[7] + '|' +board[8] + '|' +board[9])
    print('-|--|-')
    print(board[4]+  '|' + board[5] + '|' + board[6])
    print('-|--|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O' :
        marker = input('Pleace chooce marker X or O ?: ').upper()
    player_1 = marker
    if player_1 == 'X':
        player_2='O'
    else:
        player_2='X'
    return (player_1,player_2)




# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position]=marker


#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    return( (board[7]==board[8]==board[9]==mark)or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark)
    )


# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.


import random


def choose_first():
    if random.randint(0,1)==1:
        return 'player 1'
    else:
        return 'player 2'


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position]== ' '


#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    else:
        return True


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position (1-9) : '))
    return position


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    choice = input('Do you want play again yes or no ? :')
    return choice == 'yes'

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

print('Welcome to Tic Tac Toe!')

# while True:
    # Set the game up here
     # pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break
