import functions as fun
import sys
def main():
    args = (sys.argv)
    inputFile= str(args[1])
    outputFile= str(args[2])
    depth = int(args[3])
    try:
        root = fun.getFileContent(inputFile)
        child_branch,children= fun.run('opening','minimax',root,depth,True)
        print("child : ",child_branch)
        #fun.writeToFile(outputFile,children[child_branch])
    except Exception as e:
        print("An Error occured :",e)

if __name__ == "__main__":
	main()
