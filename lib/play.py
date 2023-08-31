import os
from lib.draw import CheckDraw
from lib.playerturn import PlayerTurn
from lib.computerturn import ComputerTurn
from lib.displayBoard import displayBoard
from lib.checkPlayers import Players
from lib.winners import *
from lib.undo import UndoMove


def Play(StartGame, board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr):
    isPlaying = True
    turn = 0
    while isPlaying:
        playerTurnCheck = Players(StartGame)
        if playerTurnCheck == 202:
            print("\nNo 2 Computers allowed")
            return
        print("")
        if playerTurnCheck[turn][0] == "C":
            os.system("cls || clear")
            print("\nComputer's Turn")
            print("")
            coordinates = ComputerTurn(board, boardSize, history, columnArr, diagonalArr, antiDiagonalArr)
            displayBoard(board)

        else:
            print(f"\nPlayer Turn - {playerTurnCheck[turn][0]}")
            print("")
            coordinates = PlayerTurn(
                playerTurnCheck, turn, board, history, boardSize, columnArr, diagonalArr, antiDiagonalArr
            )
            if coordinates == "quit":
                print(f"\nPlayer {playerTurnCheck[turn][0]} left")
                isPlaying = False
                break

        os.system("cls || clear")
        displayBoard(board)
        win = CheckRowWinner(board, coordinates) or CheckColumnWinner(coordinates, columnArr) or CheckDiagonalWinner(diagonalArr) or CheckAntiDiagonalWinner(antiDiagonalArr)
        if win == True:
            if playerTurnCheck[turn][0] == "C":
                print(f'\nComputer - {coordinates["Symbol"]} won')
            else:
                print(f'\nPlayer {playerTurnCheck[turn][0]} - {coordinates["Symbol"]} won')
            isPlaying = False
            break
        if CheckDraw(history, boardSize) == True:
            print("\nIt's a Draw. No one won")
            isPlaying = False
            break
        if playerTurnCheck[turn][0] != "C":
            isUndo = input("Whether u want to undo the move? (y/n) : ")
            while isUndo != "y" and isUndo != "n":
                print("\nEnter valid input")
                isUndo = input("Whether u want to undo the move? (y/n) : ")
            if isUndo == "y":
                print("\nUndoing the move")
                checkUndo = UndoMove(StartGame, history, board, turn, columnArr, diagonalArr, antiDiagonalArr)
                if checkUndo != "None":
                    os.system("cls || clear")
                    displayBoard(board)
        os.system("cls || clear")
        displayBoard(board)
        if playerTurnCheck[turn][0] == "C" or isUndo == "n":
            if turn < len(playerTurnCheck) - 1:
                turn = turn + 1
            else:
                turn = 0