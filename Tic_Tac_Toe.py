'''
DOCSTRING: Tic Tak Toe game
INPUT: Players decide X or O
OUTPUT: Depend of the choice one of the player will gonna win the game
'''
import time
# INITIAL DEFINITION OF THE ELEMENTS
player1 = ''
player2 = ''
test_board = ['#','-','-','-',    '-','-','-',    '-','-','-']


#CREATING LOGIC OF (ROCK, PAPPER, SCISSORS) TO FIND WHO IS GONNA HAVE FIRST CHOICE
def who_is():
    game = True
    while game:
        print('Let`s find who will have first choice')
        global player1, player2
        player1 = input('PLAYER 1: \nWhat you choice, "Rock", "Paper" or "Scissors" ? ').lower()
        print('\n' * 100)
        player2 = input('PLAYER 2: \nWhat you choice, "Rock", "Paper" or "Scissors" ? ').lower()
        print('\n' * 100)
        if player1.startswith('r') and player2.startswith ('s'):
            print('PLAYER 1 will have first choice using X')
            player1 = 'X'
            player2 = 'O'
            break

        elif player1.startswith('r') and player2.startswith ('p'):
            print('PLAYER 1 will have first choice using X')
            player1 = 'X'
            player2 = 'O'
            break

        elif player1.startswith('p') and player2.startswith('s'):
            print('PLAYER 2 will have first choice using X')
            player1 = 'O'
            player2 = 'X'
            break

        elif player1.startswith('p') and player2.startswith ('r'):
            print('PLAYER 2 will have first choice using X')
            player1 = 'O'
            player2 = 'X'
            break

        elif player1.startswith('s') and player2.startswith ('r'):
            print('PLAYER 2 will have first choice using X')
            player1 = 'O'
            player2 = 'X'
            break

        elif player1.startswith('s') and player2.startswith ('p'):
            print('PLAYER 1 will have first choice using X')
            player1 = 'X'
            player2 = 'O'
            break

        elif player1.startswith('r') and player2.startswith ('r'):
            print('EQUALITY!!! It`s not define who will have first choice')

        elif player1.startswith('s') and player2.startswith ('s'):
            print('EQUALITY!!! It`s not define who will have first choice')

        elif player1.startswith('p') and player2.startswith ('p'):
            print('EQUALITY!!! It`s not define who will have first choice')

    time.sleep(3)


# INTRO TO THE GAME
def intro():
    print('Hello to the game Tic Tac Toe\nTo play, each Player have to choice X or O\n'
          'on board\n'
          '1 | 2 | 3\n'
          '4 | 5 | 6\n'
          '7 | 8 | 9\n'
          '_________\n'
         )
    who_is()


# CREATING BOARD FOR PLAYING THE GAME AND DETERMINE WHO WON
def board(game_table):
    winner1 = 'Player 1'
    winner2 = ' Player 2'
    print('\n' * 100)
    print(game_table[1], '|', game_table[2], '|', game_table[3])
    print(game_table[4], '|', game_table[5], '|', game_table[6])
    print(game_table[7], '|', game_table[8], '|', game_table[9])
    print('_________')

    X_game = winning(test_board,'X')
    O_game = winning(test_board,'O')

    if X_game == True and 'X' == player1:
        print(f'Congratulation {winner1 }, You WON THE GAME!!!') 
        time.sleep(3)
        replay()
    elif X_game == True and 'X' == player2:
        print(f'Congratulation {winner2 }, You WON THE GAME!!!') 
        time.sleep(3)
        replay()

    if O_game == True and 'O' == player1:
        print(f'Congratulation {winner1 }, You WON THE GAME!!!') 
        time.sleep(3)
        replay()

    elif O_game == True and 'O' == player2:
        print(f'Congratulation {winner2}, You WON THE GAME!!!')
        time.sleep(3)
        replay()


# CREATING LOGIC OF THE PLAYER 1 INPUTS
def inputs_player1():
    if play1 == 1:
        test_board[1] = player1
        (board(test_board))
    if play1 == 2:
        test_board[2] = player1
        (board(test_board))
    if play1 == 3:
        test_board[3] = player1
        (board(test_board))
    if play1 == 4:
        test_board[4] = player1
        (board(test_board))
    if play1 == 5:
        test_board[5] = player1
        (board(test_board))
    if play1 == 6:
        test_board[6] = player1
        (board(test_board))
    if play1 == 7:
        test_board[7] = player1
        (board(test_board))
    if play1 == 8:
        test_board[8] = player1
        (board(test_board))
    if play1 == 9:
        test_board[9] = player1
        (board(test_board))

# CREATING LOGIC OF THE PLAYER 1 INPUTS
def inputs_player2():
    if play2 == 1:
        test_board[1] = player2
        (board(test_board))
    if play2 == 2:
        test_board[2] = player2
        (board(test_board))
    if play2 == 3:
        test_board[3] = player2
        (board(test_board))
    if play2 == 4:
        test_board[4] = player2
        (board(test_board))
    if play2 == 5:
        test_board[5] = player2
        (board(test_board))
    if play2 == 6:
        test_board[6] = player2
        (board(test_board))
    if play2 == 7:
        test_board[7] = player2
        (board(test_board))
    if play2 == 8:
        test_board[8] = player2
        (board(test_board))
    if play2 == 9:
        test_board[9] = player2
        (board(test_board))

# VERIFY IF THE POSITION ON THE BOARD IS FREE
def free_board(board,position,pos):
    if (board[position]=='-') and (board[pos]=='-'):
        return True


# FUNCTION THAT VERIFY IF GAME IS EQUAL OR NOT
def board_verify(board):
    x=0
    y= 0
    for i in board:
        if i =='X':
            x+=1
        elif i =='O':
            y+=1
        if (x==5 and y==4) or (x==4 and y==5):
            print('Game is EQUAL!!!')
            replay()


# CREATING LOGIC OF THE GAME
def game_logic():
    global play1,play2
    sign = True
    while sign:
        # in case if player1 have 1 choice
        if player1 == 'X':
            # 1 game
            pts = 0
            pts2 = 0
            while pts and pts2 not in [1,2,3,4,5,6,7,8,9] or not free_board(test_board,pts,pts2):
                play1 = int(input('PLAYER 1: What you choice? '))
                if pts > 0 and pts2 > 0 and pts==pts2:
                    print('Choice another position')
                    play2 = int(input('PLAYER 1: What you choice? '))
                pts = play1
                (board(test_board))
                inputs_player1()
                board_verify(test_board)
                play2 = int(input('PLAYER 2: What you choice? '))
                pts2 = play2
                if pts > 0 and pts2 > 0 and pts == pts2:
                    print('Choice another position')
                    play2 = int(input('PLAYER 2: What you choice? '))
                (board(test_board))
                inputs_player2()

                board_verify(test_board)

        # in case if player2 have 1 choice
        if player2 == 'X':
            # 1 game
            pts3 = 0
            pts4 = 0
            while pts4 and pts4 not in[1,2,3,4,5,6,7,8,9] or not free_board(test_board,pts3,pts4):
                play2 = int(input('PLAYER 2: What you choice? '))
                if pts3 > 0 and pts4 > 0 and pts3 == pts4:
                    print('Choice another position')
                    play2 = int(input('PLAYER 2: What you choice? '))
                pts3 = play2
                (board(test_board))
                inputs_player2()
                board_verify(test_board)
                play1 = int(input('PLAYER 1: What you choice? '))
                pts4 = play1
                if pts3 > 0 and pts4 > 0 and pts3 == pts4:
                    print('Choice another position')
                    play2 = int(input('PLAYER 1: What you choice? '))
                (board(test_board))
                inputs_player1()
                board_verify(test_board)


# VERIFY WINNING PATTERN IF IS ACHIEVED
def winning(test,enter):
    return ((test[1]== enter and test[2]==enter and test[3] == enter) or # across the top
            (test[4]== enter and test[5]==enter and test[6] == enter) or # across the middle
            (test[7] == enter and test[8] == enter and test[9] == enter) or # across bottom
            (test[1]== enter and test[5]==enter and test[9] == enter)or # diagonal
            (test[1]== enter and test[4]==enter and test[7] == enter) or # across left column
            (test[2]== enter and test[5]==enter and test[8] == enter) or # across middle column
            (test[3]== enter and test[6]==enter and test[9] == enter) or# across right column
            (test[3]== enter and test[5]==enter and test[7] == enter)) # # diagonal

# GAME REPLAY FUNCTION
def replay():
    global test_board
    answer = True
    while answer:
        a = input('Do you want to replay, Yer or No?').lower()
        if a.startswith('y'):
            test_board = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            print('\n' * 100)
            who_is()
            board(test_board)
            game_logic()

        elif a.startswith('n'):
            print('Thanks for playing the Tic Tac Toe Game')
            quit()

# RUNNING THE GAME
(intro())
(board(test_board))
(game_logic())

