board = ['-'] * 9
def show_board():
    for i in range(0, 7, 3):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2])

def validation(input_position):
    if input_position > 9 or input_position <= 0:
        return False
    else:
        if board[input_position - 1] != '-':
            return False
        else:
            return True


def take_input(msg):
    input_position = int(input(msg))
    while not validation(input_position):
        print("invalid number, please try again")
        input_position = int(input(msg))
    return input_position


def check_winner(board):
    row1Sum = row2Sum =row3Sum=0
    col1Sum = col2Sum = col3Sum = 0
    d1 = d2 = 0

    if board[0].isdigit() and board[1].isdigit() and board[2].isdigit():
        row1Sum = int(board[0])+int(board[1])+int(board[2])
    if board[3].isdigit() and board[4].isdigit() and board[5].isdigit():
        row2Sum = int(board[3])+int(board[4])+int(board[5])
    if board[6].isdigit() and board[7].isdigit() and board[8].isdigit():
        row3Sum = int(board[6])+int(board[7])+int(board[8])

    if board[0].isdigit() and board[3].isdigit() and board[6].isdigit():
        col1Sum = int(board[0])+int(board[3])+int(board[6])

    if board[1].isdigit() and board[4].isdigit() and board[7].isdigit():
        col2Sum = int(board[1])+int(board[4])+int(board[7])

    if board[2].isdigit() and board[5].isdigit() and board[8].isdigit():
        col3Sum = int(board[2])+int(board[5])+int(board[8])


    if board[0].isdigit() and board[5].isdigit() and board[8].isdigit():
        d1 = int(board[0])+int(board[5])+int(board[8])

    if board[2].isdigit() and board[4].isdigit() and board[6].isdigit():
        d2 = int(board[2])+int(board[4])+int(board[6])


    if row1Sum == 15 or row2Sum == 15 or row3Sum == 15 or col1Sum == 15 or col2Sum == 15 or col3Sum == 15 or d1 == 15 or d2 ==15:
        return True
    else:
        return False

def game():
    moves = 0
    while True:
        show_board()
        print("choose position from 1 -> 9: ")
        player1_position = take_input("player1 position: ")
        print("choose a number from [1,3,5,7,9]: ")
        player1_input = (input("player1 input: "))
        board[player1_position - 1] = player1_input
        moves +=1
        if check_winner(board):
            show_board()
            print("Player One Wins")
            break
        if moves == 9:
            print("Draw")
            break
        show_board()
        print("choose position from 1 -> 9: ")
        player2_position = take_input("player2 position: ")
        print("choose a number from [0,2,4,6,8]: ")
        player2_input = (input("player2 input: "))
        board[player2_position - 1] = player2_input
        moves +=1
        if check_winner(board):
            show_board()
            print("Player Two Wins")
            break
game()
