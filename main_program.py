import functions as fun
import sys
def main():
    args = (sys.argv)
    inputFile= str(args[1])
    outputFile= str(args[2])
    depth = int(args[3])
    try:
        root = fun.getFileContent(inputFile)
        child_branch= fun.MiniMax(root,depth,True)
        children = fun.GenerateMovesOpening(root)
        fun.writeToFile(outputFile,children[child_branch])
    except Exception as e:
        print("An Error occured :",e)

if __name__ == "__main__":
	main()
