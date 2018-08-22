import sys
board = list(range(1,10))
print(board)

def print_fresh_board():
    board = list(range(1,10))
    print(len(board))
    count = 0
    for iterator in board:
        if((count + 1) % 3 == 0):
            print(board[count], end = '\n')
            count= count + 1
        else:
            print(board[count], end = ' ')
            count=count + 1
    print("The X plays first. ")

def check_win(marker):
    if(board[0] == board[1] == board [2] == marker or board[3] == board[4] == board [5] == marker or board[6] == board[7] == board [8] == marker):
        print(marker, " wins")
        return 1
    elif(board[0] == board[4] == board[8] == marker or board[2] == board[4] == board[6] == marker):
        print(marker, "wins")
        return 1
    elif(board[0] == board[3] == board[6] == marker or board[1] == board[4] == board[7] == marker or board[2] == board[5] == board[8] == marker):
        print(marker, "wins")
        return 1
    else:
        return 0

def take_input():
    print("choose the place")
    inp = input("> ")
    if(ord(inp) < 47 or ord(inp) > 58):
        print("Please try again")
        take_input()
    x = int(float(inp))
    return x-1

def display_the_board():
    count = 0
    for iterator in board:
        if((count + 1) % 3 == 0):
            print(board[count], end = '\n')
            count= count + 1
        else:
            print(board[count], end = ' ')
            count=count + 1

def place_the_marker(marker, position):
    board[position] = marker
    display_the_board()

def play_board():
    marker = 'X'
    choice = 'Y'
    print_fresh_board()
    count = 0
    for iterator in board:
        if((count) % 2 == 0):
            count = count + 1
            marker = 'X'
            print("\n X's turn, ")
        else:
            marker = 'O'
            count = count + 1
            print("\n O's turn, ")
        position = take_input()
        place_the_marker(marker, position)
        status = check_win(marker)
        if(status == 0 and count == 8):
            print("A mess is made")
            choice = input("Want to play again ? > ")
            play_again(choice)
        elif(status == 1):
            choice = input("Want to play again ? > ")
            play_again(choice)



def play_again(choice):
    if(choice == 'Y' or choice == 'y'):
        play_board()
    else:
        print("Great Game!")

play_board()

# TODO:add tuple for immutable string
