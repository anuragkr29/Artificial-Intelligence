import functions
import sys
def main():
    args = (sys.argv)
    inputFile= str(args[1])
    outputFile= str(args[2])
    depth = int(args[3])
    try:
        root = functions.getFileContent(inputFile)
        child_branch, children= functions.run('midgame','alphabeta', root,depth,True)
        print("here : ",child_branch)
        #functions.writeToFile(outputFile,children[child_branch])
    except Exception as e:
        print("An Error occured :",e)

if __name__ == "__main__":
	main()
