from functions import morrisGame
import IO


def main():
    root, outputFile, depth = IO.getInput()
    try:
        game = morrisGame()
        root = game.blackMove(root)
        estimate, next_move= game.run('opening', 'minimax', root, depth, True)
        next_move = game.blackMove(next_move)
        IO.writeToFile(outputFile, next_move)
        game.printOutput(estimate, 'MiniMax')
    except Exception as e:
        print("An Error occured :",e)


if __name__ == "__main__":
    main()
