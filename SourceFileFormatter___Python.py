import os
NUM_SPACES_INDENT = 4
FILE_PATH = "test/"

class Processor:

    #Function reads file and outputs content as a list of words
    def readFromFile(self, filename): 
        with open(filename) as inputFile:
            testFile = inputFile.read()
        
        return testFile

    #Function that creates a file and writes an input to it
    def createAndWriteToFile(self, filename, input): 
        with open(filename, "w+") as outputFile:
            outputFile.write(input)

    #Static function returning number of spaces according to level of indentation
    @staticmethod
    def indent(level):
        return " " * NUM_SPACES_INDENT * level

    #Main processing function that uses fstrings to format the source file text by checking each character for format specifiers
    def processText(self, txt):
        out_txt = ""
        indentationLevel = 0 

        for ch in txt:
            if ch == '(':
                out_txt += f"{ch} "
            elif ch == ')':
                out_txt += f" {ch}"
            elif ch == '{':
                out_txt += f"\n{Processor.indent(indentationLevel)}{ch}\n"
                indentationLevel += 1
                out_txt += Processor.indent(indentationLevel)
            elif ch == '}':
                indentationLevel -= 1
                out_txt += f"\n{Processor.indent(indentationLevel)}{ch}\n"
                out_txt += Processor.indent(indentationLevel)
            elif ch == '\n':
                out_txt += f"{ch}{Processor.indent(indentationLevel)}"
            elif ch == '#' :
                out_txt += f"\n{ch}"
            elif ch == ';':
                out_txt += f"{ch}\n"
            
            #Checking for comments proves troublesome as there have to be two backslashed in a row to denote a comment        
            elif ch == '//':
                out_txt += f"\n{ch}"
            else:
                out_txt += ch

        return out_txt

if __name__ == "__main__":

    processor = Processor()

    print("This tool will correctly format any source file in a C-type language.\n")
    print("-" * 50)

    tryAgain = True

    #Loop that provides functionality of the menu
    while tryAgain:

        fileName = input("\nEnter the filename for a source file in the test folder to process including extension: ")

        #Filename given is checked and its existence dictates the rest of the program flow
        exists = os.path.exists(FILE_PATH + fileName)

        #If file exists, it can be manipulated
        if exists:

            testFile = processor.readFromFile(FILE_PATH + fileName)

            out_txt = processor.processText(testFile)

            outcomeChoice = input("\nFile has been processed, would you like to print, save or exit without saving? (print/save/exit)\n")

            if outcomeChoice == 'Save' or outcomeChoice == 'save':

                outputName = input("\nPlease enter filename to be saved including extension\n")

                processor.createAndWriteToFile(FILE_PATH + outputName, out_txt)
                
                toggleLoop = input("\nFile has been saved.Would you like to try again? (Y/N)")

                if toggleLoop == 'Y' or toggleLoop == 'y':
                    tryAgain = True
                else:
                    tryAgain = False

            elif outcomeChoice == 'Print' or outcomeChoice == 'print':

                print(out_txt)

                toggleLoop = input("\nWould you like to try again? (Y/N)")

                if toggleLoop == 'Y' or toggleLoop == 'y':
                    tryAgain = True
                else:
                    tryAgain = False

            else:
                print("\n-" * 50)
                print("\nProgram has now stopped")
                exit(0)
             
        #If file doesn't exist, the user is given a choice to try again
        elif not exists:
            print("-" * 50)
            print("\nFile cannot be found!")
            toggleLoop = input("\nWould you like to try again? (Y/N)")

            if toggleLoop == 'Y' or toggleLoop == 'y':
                tryAgain = True
            else:
                tryAgain = False
    
    print("-" * 50)
    print("\nProgram has now stopped")
    exit(0)                