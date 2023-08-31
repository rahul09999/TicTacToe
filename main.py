from lib.checkPlayers import Players
from lib.createBoard import createBoard
from lib.displayBoard import displayBoard
from lib.play import Play
import os

if __name__ == "__main__":
    os.system("cls||clear")
    while True:
        userInput = input(
            '''
            Input_Format:- [Total_Players] [...userID and Symbol of each player separated by space...] [boardSize] :

        *Note: Make sure format remaines same and For computer, userId anf Symbol both should be "C"
                        
        eg. 2 u1 O u2 X 3 :   ''')
        userInput = userInput.strip().split()
        
        # Validate input of user
        #Case1: totalPlayers and BoardSize should be number
        if userInput[0].isdigit() & userInput[len(userInput)-1].isdigit():
            #Case2: totalPlayers should be equal to number of players
            if int(userInput[0]) == len(userInput[1:-1])/2:
                break
            else:
                print("\nPlease enter correct number of players and symbols")
                continue
        else:
            print("\nWarning: Enter number of players and board size in number only")
            continue

    validateUser = Players(userInput)
    # print(validateUser)
    if type(validateUser) != type([]):
        if type(validateUser) == type("string"):
            print(validateUser)
            exit()
    else:
        if len(validateUser) != int(userInput[0]):
            print("Error: Please enter correct equal number of players, userId and symbol")
            exit()

    boardSize = int(userInput[len(userInput)-1])
    board = []
    columnArray = []
    daigonalArray = []
    antiDaigonalArray = []
    history = []

    def handleColumnArray(columnArray, board):
        boardLength = len(board)
        for i in range(boardLength):
            columnArray.append([])
            for j in range(boardLength):
                columnArray[i].append(" ")
        return columnArray

    def handleDaigonalArray(daigonalArray, board):
        boardLength = len(board)
        for i in range(boardLength):
            daigonalArray.append(" ")
        return daigonalArray 

    createBoard(board, boardSize)
    handleColumnArray(columnArray, board)
    handleDaigonalArray(daigonalArray, board)
    handleDaigonalArray(antiDaigonalArray, board)
    displayBoard(board)
    Play(userInput, board, boardSize, history, columnArray, daigonalArray, antiDaigonalArray)
        




