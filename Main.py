from random import randint
from Functions import *
 
#Initializing the board
board = []
board_dim = 10
ships = 0
blank_char = (".")
ship_char = ("S")
miss_char = ("O")
hit_char = ("X")
for x in range(board_dim):
    board.append([blank_char] * board_dim)
 
player_board = board
board_key = board
 
#Placing the ships
place_ship(board_key,5,"A",blank_char) #Aircraft Carrier
place_ship(board_key,4,"B",blank_char) #Battleship
place_ship(board_key,3,"S",blank_char) #Submarine
place_ship(board_key,3,"D",blank_char) #Destroyer
place_ship(board_key,2,"P",blank_char) #Patrol Boat




ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board[0]) - 1)
print (ship_row)
print (ship_col)
 
#Beginning Greeting
print ("Let's play Battleship!")
print_board(board_key)
 
                
   
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
   
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
   
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == hit_char):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = hit_char
            if turn == 3:
                print ("Game Over")
        # Print (turn + 1) here!
        print (str(turn+1))
        print_board(board)
