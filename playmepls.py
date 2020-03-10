
'''
The main method simply begins by greeting the player. Then proceeds to start the game via a while loop and multiple if conditions.
The if conditions check if X or O wins the game by checking the alignment of the letters according to a preset algorithm.

'''

def main():
    print('Welcome to Tic Tac Toe, lets do this!')
    printbrd(brd)

    while not(checkfull(brd)):
        if not(checkifwinner(brd, 'O')):
            playerMove()
            printbrd(brd)
        else:
            print('Good job O, you have won this time!')
            break

        if not(checkifwinner(brd, 'X')):
            move = ai()
            if move == 0:
                print('So it ends in a draw!')
            else:
                insertLetter('O', move)
                print('I, the system have placed an \'O\' in position', move , ':')
                printbrd(brd)
        else:
            print('Good job X, you have won this time!')
            break


def insertLetter(letter, pos):
    brd[pos] = letter

def spaceIsFree(pos):
    return brd[pos] == ' '

def printbrd(brd):
    print('   |   |')
    print(' ' + brd[1] + ' | ' + brd[2] + ' | ' + brd[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + brd[4] + ' | ' + brd[5] + ' | ' + brd[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + brd[7] + ' | ' + brd[8] + ' | ' + brd[9])
    print('   |   |')
    
def checkifwinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def ai():
    possibleMoves = [x for x, letter in enumerate(brd) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            brdCopy = brd[:]
            brdCopy[i] = let
            if checkifwinner(brdCopy, let):
                move = i
                return move

    open_corners = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            open_corners.append(i)
            
    if len(open_corners) > 0:
        move = randomsel(open_corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = randomsel(edgesOpen)
        
    return move

def randomsel(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def checkfull(brd):
    if brd.count(' ') > 1:
        return False
    else:
        return True


while True:
    answer = input('Wanna play again maybe ? (Yes/No) ')
    if answer == 'Yes' or answer == 'yes':
        brd = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break


    brd = [' ' for x in range(10)]
