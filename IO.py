import os
import sys

def getInput():
    args = (sys.argv)
    try:
        inputFile, outputFile, depth = [arg for arg in args[1:]]
        return getFileContent(inputFile), str(outputFile), int(depth)
    except Exception as e:
        print("Input Error :", e)

def getFileContent(fName):
    if os.path.exists(fName):
        with open(fName, 'r') as f:
            try:
                file_content = f.read()
                print("Input position   : {}".format(file_content),)
                return file_content
            except :
                print('Error opening the file')
                sys.exit()
            finally:
                f.close()


def writeToFile(fOut, file_content):
    try:
        with open(fOut, 'w') as dest:
            dest.write(file_content)
            print("Output position  : {}".format(file_content))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
        sys.exit()
    finally:
        dest.close()