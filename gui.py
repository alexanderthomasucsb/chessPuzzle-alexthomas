import tkinter as tkin

import random
import os.path



root = tkin.Tk()
root.title("Alex's Chess Puzzle")
root.geometry("1300x1000")

header = tkin.Label(root,text="2D Chess",)
header.config(font=("courier",20))
header.grid(column=0,row=0)

def roundLabel():
        global moveNo

        roundText = tkin.Label(root,text="MOVE")
        roundNo = tkin.Label(root,text=moveNo)
        roundText.grid(column=0,row=9,sticky="w")
        roundNo = roundNo.grid(column=0,row=9)

        #return moveNo
        #active.calculateMove(board,boardObjectSpaces)

def playerLabel(playerGo):
        pass

def labelTop():
        #putting letter labels at top of board
        topLabels = ["A","B","C","D","E","F","G","H"]
        count=1
        for letter in topLabels:
                letter = tkin.Label(root,text=letter)
                letter.grid(column=count,row=0,sticky="S")
                count+=1

def labelSide():
        #putting numbers in labels at side of board
        sideLabels = []
        sideLabels+= range(8,0,-1)
        count=1
        for num in sideLabels:
                num = tkin.Label(root,text=num)
                num.grid(column=0,row=count,sticky="E")
                count+=1

def padding():        
        #left padding #####################
        lLabel = tkin.Label(root)
        lLabel.grid(column=0,ipadx=50)

def makeBoardCanvases():
        '''Gets and stores the square images needed to make the board'''
        #because ImageTk garbage collects after function is finished
        #you must make your image variables global
        #global b
        #global w
        #b = Image.open("mats/blackSquare.jpg")
        #w = Image.open("mats/whiteSquare.jpg")
        #global bImg
        #global wImg
        #bImg = ImageTk.PhotoImage(b)
        #wImg = ImageTk.PhotoImage(w)

        global blackSquares
        global whiteSquares
        #black squares
        blackSquares = []
        blackSquares+=range(0,32)

        #white squares
        whiteSquares = []
        whiteSquares+=range(0,32)

        #assigning images to the variables inside square lists using their indexes
        #USING CANVASES instead
        #images of the pieces can be pasted inside canvases with coloured backgrounds
        #this preserves transparency and makes it easier
        for var in blackSquares:
            ind = blackSquares.index(var)
            blackSquares[ind] = tkin.Canvas(root, width=110,height=110,border=0,bg="brown",cursor="hand2")
            #blackSquares[ind].create_image(50,50,image=)
            
        for var in whiteSquares:
            ind = whiteSquares.index(var)
            whiteSquares[ind] = tkin.Canvas(root, width=110,height=110,border=0,bg="white",cursor="hand2")
            #whiteSquares[ind].create_image(50,50,image=)
            
        return blackSquares,whiteSquares
        

def positionBoardCanvases(blackSquares,whiteSquares):
        '''Positions the square images into grid columns and rows'''
        #Below uses indexes to pick & position square image objects into a grid
        #the ranges change because the indexes contain different objects
        ################change this to be valid with
        #each chunk is one row
        bCol = 0
        wCol = -1
        for num in range(0,4):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=1)
            whiteSquares[num].grid(column=wCol,row=1)

        bCol = -1
        wCol = 0
        for num in range(4,8):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=2)
            whiteSquares[num].grid(column=wCol,row=2)

        bCol = 0
        wCol = -1
        for num in range(8,12):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=3)
            whiteSquares[num].grid(column=wCol,row=3)

        bCol = -1
        wCol = 0
        for num in range(12,16):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=4)
            whiteSquares[num].grid(column=wCol,row=4)

        bCol = 0
        wCol = -1
        for num in range(16,20):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=5)
            whiteSquares[num].grid(column=wCol,row=5)

        bCol = -1
        wCol = 0
        for num in range(20,24):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=6)
            whiteSquares[num].grid(column=wCol,row=6)

        bCol = 0
        wCol = -1
        for num in range(24,28):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=7)
            whiteSquares[num].grid(column=wCol,row=7)

        bCol = -1
        wCol = 0
        for num in range(28,32):
            bCol+=2
            wCol+=2
            blackSquares[num].grid(column=bCol,row=8)
            whiteSquares[num].grid(column=wCol,row=8)

        return blackSquares,whiteSquares

def boardSpaces(blackSquares,whiteSquares):
        #BOARD SPACES LIST
        #Merging blackSquares and whiteSquares together in an accurate index representation
        #63 total index spaces with a 0
        #32 black squares and 32 white squares
        #Because each row swaps square colour patterns from white black to black white the algorithm has to do this too
        #Leave this unindented otherwise the index spaces will mess up going downwards in 2 columns
        board = []
        for num in range(0,4):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(4,8):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(8,12):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(12,16):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(16,20):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(20,24):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        for num in range(24,28):
                board.append(whiteSquares[num])
                board.append(blackSquares[num])
        for num in range(28,32):
                board.append(blackSquares[num])
                board.append(whiteSquares[num])
        return board


#boardobjectspaces will store objects in the index that matches their position on the board
#one can then access their color through object.color
#IMPORTANT
# example = [bpawn1,wqueen,bpawn2]
boardObjectSpaces = []
for num in range(0,64):
        boardObjectSpaces.append("")


#SETS
#global variables
#stores pieces which are objects
wSet = []
bSet = []

class Piece(object):
        def __init__(self,color,mySet):
                #things that never change after initialisation
                #color of the piece
                self.color = color
                #once object is created append it into its set
                self.mySet = mySet.append(self)
        
        #properties
        alive = True
        squareInd = 0
        #####move below outside of class
        #if self.color == "b":
                #square = board[squareInd].create_image(55,55,image=self.bImage)
        #elif self.color == "w":
                #square = board[squareInd].create_image(55,55,image=self.wImage)


        # these globals represent rows and columns on the board
        # they are used for the moves() method in each piece subclass to determine where
        # a piece can move depending on where they are on the board
        global row1
        global row2
        global row3
        global row4
        global row5
        global row6
        global row7
        global row8

        global col1
        global col2
        global col3
        global col4
        global col5
        global col6
        global col7
        global col8

        row1 = range(0, 8)
        row2 = range(8, 16)
        row3 = range(16, 24)
        row4 = range(24, 32)
        row5 = range(32, 40)
        row6 = range(40, 48)
        row7 = range(48, 56)
        row8 = range(56, 64)

        col1 = range(0, 57, +8)
        col2 = range(1, 58, +8)
        col3 = range(2, 59, +8)
        col4 = range(3, 60, +8)
        col5 = range(4, 61, +8)
        col6 = range(5, 62, +8)
        col7 = range(6, 63, +8)
        col8 = range(7, 64, +8)

        def unbindAll(self):
                pass

class Pawn(Piece):
        #properties
        

        kind = "pawn"


        def moves(self,squareIndex):
                print("PAWN MOVE")
                #index of current square in boardSquares
                print(squareIndex,"\n")

                piece = boardObjectSpaces[squareIndex]

                #plug base movements into list
                #left = squareIndex - 1
                #right = squareIndex + 1
                up = squareIndex - 8
                up2 = up - 8
                nw = squareIndex - 9
                ne = squareIndex - 7

                #sw = squareIndex + 7
                #se = squareIndex + 9
                #down = squareIndex + 8
                #possibleSpaces = [left,right,up,down]

                #both are upside down to eachother
                if self.color == "w":
                        up = squareIndex - 8
                        nw = squareIndex - 9
                        ne = squareIndex - 7
                        up2 = up - 8

                elif self.color == "b":
                        up = squareIndex + 8
                        nw = squareIndex + 7
                        ne = squareIndex + 9
                        up2 = up + 8


                possibleSpaces = [up, nw, ne]

                #lets pawns do a double move on their first move
                if self.color == "w":
                        for space in row7:
                                print(space)
                                if boardObjectSpaces.index(self) == space:
                                        possibleSpaces.append(up2)
                if self.color == "b":
                        for space in row2:
                                if boardObjectSpaces.index(self) == space:
                                        possibleSpaces.append(up2)


                #make sure the piece isn't on row ends
                #if it is then remove appropriate move from list of moves
                #if squareIndex in range(0,56,+8):
                        #can't go left
                        #possibleSpaces.remove(left)
                #if squareIndex in range(7,63,+8):
                        #can't go right
                        #possibleSpaces.remove(right)

                ########
                #if squareIndex in range(0,8):
                        #can't go up
                        #possibleSpaces.remove(up)

                #if squareIndex in range(56,63):
                        #can't go down
                        #possibleSpaces.remove(down)


                origSquare = board[squareIndex]
                #print(origSquare)

                copyPossibleSpaces = possibleSpaces

                print(copyPossibleSpaces)

                ##########
                playColor = boardObjectSpaces[squareIndex].color

                # used to store spaces we will delete
                deleteSpaces = []

                # print(boardObjectSpaces)

                # determining the bunch of spaces that must be removed if counter is blocking the line of sight
                #need to use deletespaces otherwise I would mess up the for loop by editing it (copypossiblespaces) while looping it
                for var in copyPossibleSpaces:
                        if var == up:
                                if boardObjectSpaces[var] != "":
                                        deleteSpaces.append(up)
                                        deleteSpaces.append(up2)
                                else:
                                        pass
                        if var == up2:
                                if boardObjectSpaces[var] != "":
                                        deleteSpaces.append(up2)
                                else:
                                        pass
                        if var == nw:
                                if squareIndex in col1:
                                        deleteSpaces.append(nw)
                                else:
                                        if boardObjectSpaces[var] != "":
                                                if boardObjectSpaces[var].color == playColor:
                                                        deleteSpaces.append(nw)
                                                if boardObjectSpaces[var].color != playColor:
                                                        pass
                                        else:
                                                #if empty then can't move there
                                                deleteSpaces.append(nw)
                        if var == ne:
                                if squareIndex in col8:
                                        deleteSpaces.append(ne)
                                else:
                                        if boardObjectSpaces[var] != "":
                                                if boardObjectSpaces[var].color == playColor:
                                                        deleteSpaces.append(ne)
                                                if boardObjectSpaces[var].color != playColor:
                                                        pass
                                        else:
                                                deleteSpaces.append(ne)





                #removing spaces that are blocked
                for varia in deleteSpaces:
                        if varia in copyPossibleSpaces:
                                 copyPossibleSpaces.remove(varia)
                        else:
                                 pass

                # print(playColor)
                # print("copyPossibleSpaces", copyPossibleSpaces)


                # highlighting possible spaces in light purple
                for var in copyPossibleSpaces:
                        posSpace = board[var]
                        posSpace.config(bg="mediumpurple4")
                        # EVENT
                        # move on click
                        posSpace.bind("<Button-1>", lambda event: doMove(event,origSquare = origSquare,possibleMoves = copyPossibleSpaces))


                #EVENT
                #deselect on right click
                #lambda is necessary so arguments can be accepted inside the function inside bind()
                origSquare.bind("<Button-3>",lambda event: deselect(event,possibleSpaces = possibleSpaces))



root.mainloop()