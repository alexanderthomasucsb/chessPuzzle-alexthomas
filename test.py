


columnLetterToCoord = {'a': 0,'b' : 1,'c' : 2,'d' : 3,'e' : 4,'f' : 5,'g' : 6,'h' : 7 }


def puzzleNotationToCoord(puzzleNotationList):
    tempArray = []
    for place in puzzleNotationList:
        coord = (8-int(place[2]))*8 + columnLetterToCoord[place[1]]
        tempArray.append(place[0]+ str(coord))
    return tempArray
        





def setUpFromFile():
    #opens puzzle text file and turns it into a string
    text_file = open("/Users/alexanderthomas/Desktop/passionProject-alexthomas/puzzle1.txt", "r")
    puzzle = text_file.read()
    text_file.close()

    #seperates the puzzle string into arrrays containing the black pieces setup, white pieces set up and the solution
    x=puzzle.split("\n")
    bSetUp = x[0][3:].split(',')
    wSetUp = x[1][3:].split(',')
    solution = x[2][3:].split(',')

    
    bSetupCoord = puzzleNotationToCoord(bSetUp)
    print(bSetupCoord)




    
    

    




    
setUpFromFile()
