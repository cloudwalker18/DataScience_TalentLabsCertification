#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    
    position = int(position)
    board[position] = mark
    return board


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    for k, v in board.items():
        if v != ' ':
            board[k] = v
        else:
            board[k] = str(k)
    print("\t")
    print("\t"+ board[1] + " | " + board[2] + " | " + board[3])
    print("\t---------")
    print("\t"+ board[4] + " | " + board[5] + " | " + board[6])
    print("\t---------")
    print("\t"+ board[7] + " | " + board[8] + " | " + board[9])
    print("\t")


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = int(position)
    if (position < 1) or (position > 9):
        return False
    elif (board[position] == 'X' or board[position] == 'O' or board[position] == int(position)):
        return False
    else:
        return True

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    mark_list = []
    for k,v in board.items():
        if v == player:
            mark_list.append(k)
    for x in winCombinations:
      if all(y in mark_list for y in x):
        return True   

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    count = 0
    for v in board.values():
        if (v == 'X') or (v == 'O'):
            count += 1
            if count == 9:
                return True
        else:
            return False

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

while True:
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")

## User input and validate the input
        try:
            validateMove(move)
        except ValueError:
            print("Wrong Input! Please Try Again!")
            continue
        if validateMove(move) == False:
            print('Please choose another position')  
            continue

## Update the board
        else:
            markBoard(move,currentTurnPlayer)
            printBoard()        

## Check win or tie situation   
        if checkFull() == True:
          if checkWin(currentTurnPlayer) == True:
             print("\nGame Over!\n")
             print(currentTurnPlayer + " player won\n")
             gameEnded = True
          else:
             print("\nGame Over!\n")
             print("It's a tie\n")
             gameEnded = True 
        else:
           if checkWin(currentTurnPlayer) == True:
              print("\nGame Over!\n")
              print(currentTurnPlayer + " player won\n")
              gameEnded = True    

## Switch user
        if currentTurnPlayer == 'X':
            currentTurnPlayer = 'O'
        else:
            currentTurnPlayer = 'X'

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

    choice = input("\nDo you want to restart? (y/n): ")
    if choice == 'Y' or choice == 'y':
        gameEnded = False
        print('Game started: \n\n' +
                    ' 1 | 2 | 3 \n' +
                    ' --------- \n' +
                    ' 4 | 5 | 6 \n' +
                    ' --------- \n' +
                    ' 7 | 8 | 9 \n')
        for k in board.keys():
            board[k] = ' ' 
    else:
        print("Thanks for playing :)\n")
        gameEnded = True
        break