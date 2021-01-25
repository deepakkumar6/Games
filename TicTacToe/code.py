# Tic Tak Toe
board = ["-" for i in range(9)]

# display board
def display_board():
    print()
    print(' '*3,'|','---------','|',' '*3,' '*3,'|','---------','|')
    print(' '*3,'|',board[0]+' | '+board[1]+' | '+board[2],'|',' '*3,' '*3,'|','1'+' | '+'2'+' | '+'3','|')
    print(' '*3,'|','--+---+--','|',' '*3,' '*3,'|','--+---+--','|')
    print(' '*3,'|',board[3]+' | '+board[4]+' | '+board[5],'|',' '*3,' '*3,'|','4'+' | '+'5'+' | '+'6','|')
    print(' '*3,'|','--+---+--','|',' '*3,' '*3,'|','--+---+--','|')
    print(' '*3,'|',board[6]+' | '+board[7]+' | '+board[8],'|',' '*3,' '*3,'|','7'+' | '+'8'+' | '+'9','|')
    print(' '*3,'|','---------','|',' '*3,' '*3,'|','---------','|')
    print()

# check game things
def check_if_game_over():
    # Rows Check
    if (board[0]==board[1]==board[2] and board[0] in 'OX')or \
       (board[3]==board[4]==board[5] and board[3] in 'OX')or \
       (board[6]==board[7]==board[8] and board[6] in 'OX'):
       return False

    # Columns Check
    if (board[0]==board[3]==board[6] and board[0] in 'OX')or \
       (board[1]==board[4]==board[7] and board[1] in 'OX')or \
       (board[2]==board[5]==board[8] and board[2] in 'OX'):
       return False

    # Diagonal Check
    if (board[0]==board[4]==board[8] and board[0] in 'OX')or \
       (board[2]==board[4]==board[6] and board[2] in 'OX'):
       return False

    return True

def flip_player(curr_player):return 'O' if curr_player == 'X' else 'X'

def play_game():

    display_board();#initial board

    curr_player = 'X'

    game_still_going = True

    moves = 0 # Used for Tie or Not

    while game_still_going:

        player_moves(curr_player)

        game_still_going = check_if_game_over()

        if not game_still_going :

            print(curr_player,"is the winner");

            break;

        curr_player = flip_player(curr_player)

        moves+=1

        if moves==9:

            print('Game Tie')

            break;



def player_moves(curr_player):
    valid_input = False

    print(curr_player,'s, Turn')

    while not valid_input:

        print('Choose a postion from 1-9 : ')

        pos = input()
        if len(pos)==1 and ord('1')<=ord(pos)<=ord('9'):

            if board[int(pos)-1]=='-':
                valid_input = True
            else:
                print('This Position is Occupied')
    board[int(pos)-1] = curr_player
    display_board()

try_again = 1

while try_again:

    play_game()

    valid_input = False

    while not valid_input:

        print('Press 1 to Restart the Game ')
        print('Press 0 to Stop the Game')

        try:
            try_again = int(input())
            if try_again in [0,1]:
                valid_input = True
        except:
            pass
    board = ["-" for i in range(9)] # clean the board


# @ code written by Deepak Kumar
