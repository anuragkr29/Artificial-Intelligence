from functions import morrisGame
import IO


def main():
    root, outputFile, depth = IO.getInput()
    try:
        game = morrisGame()
        estimate, next_move = game.run('opening', 'alphabeta', root, depth, True)
        IO.writeToFile(outputFile, next_move)
        game.printOutput(estimate, 'AlphaBeta')
    except Exception as e:
        print("An Error occured :",e)


if __name__ == "__main__":
    main()
