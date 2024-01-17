ALL_SPACES = ['1', '2', '3', '4', '5','6', '7','8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('Welcome to Tic-Tac-Toe from invent with python')
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)
        
