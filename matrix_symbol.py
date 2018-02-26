#!usr/bin/env/python3.6
# import for create gui
from tkinter import *
# import for create matrix symbol
import numpy as np
import random
# Generated random matrix of 25 spaces, 
# where placed ramdom number between 0 to 255,
# and store in a variable.
matrix = np.random.randint(33,255, size=(5, 5))
# This translate  matrix of number to ASCII table symbols:


class program:
    def __init__(self):
        self.v = Tk() # create main window game
        self.v.title('Matrix symbol.') # give title
        self.v0 = Toplevel(self.v) # create window
        self.v0.title('Matrix 5 * 5') # give title
        self.v0.withdraw() # Hide v0
        self.v1=Toplevel(self.v) # create other window
        self.v1.title('Symbols stored.') # give title
        self.v1.withdraw() # Hide v1
        self.v2=Toplevel(self.v) # create other window
        self.v2.title('Reconstruction') # give title
        self.v2.withdraw() # Hide v2
        self.C = 5 # variables matrix
        self.R = 5
        
    def show_store(self):
        self.v1.deiconify() # show stored sort matrix
        col = self.C # car for colummn
        row = self.R # var for rows
        np.sort(matrix) # Ordered the matrix
        for r in range(row): # repeat the same proces, but for compare 
            for c in range(col): # read in columns to add buttons with symbol
                btn0=Button(self.v1,text=chr(matrix[r][c]),width=2)
                btn0.grid(row= r,column= c) # position in grid by

    
    def matrix_5_5(self):
        self.v0.deiconify() # show matrix to memorice
        col = self.C # variables
        row = self.R
        for c in range(col): # create matrix to memorized.
            for r in range(row): # create row of window
                btn0=Button(self.v0,text=chr(matrix[c][r]),width=2) # fill the buttons
                btn0.grid(row= r,column= c) # give position of buttonns in gris
    
    def reconstructor(self):
        self.v2.deiconify() # show matrix to memorice
        col = 5
        row = 5
        for r in range(row): # repeat the same proces, but for compare 
            for c in range(col): # read in columns to add buttons with symbol
                input0=Entry(self.v2, width=2)
                input0.grid(row= r,column= c) # position in grid by

    def run(self):
        # Button generator matrix
        btna = Button(self.v, text='Matrix 5*5',command=self.matrix_5_5)
        btna.grid(row=1, column=1)
        # Button remenber and sort matrix
        btnb=Button(self.v, text= 'remember', command=self.show_store)
        btnb.grid(row=1,column=2)
        # Button for input the
        btnc = Button(self.v, text='Reconstruction', command=self.reconstructor)
        btnc.grid(row=1, column=3)
        self.v.mainloop()
        
if __name__ == '__main__': # call the main program
    window=program()
    window.run()
