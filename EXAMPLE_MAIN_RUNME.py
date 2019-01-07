##############################################################
# CROSSWORD:     
# Bart McCoy
# 1/6/2018
# for Python 3.6, requiring additional modules "numpy" and "os"
# 
# OVERVIEW:
# I ALWAYS HATED SCHOOL-STYLE "CROSSWORDS" OR SIMPLY "WORD SEARCHES".
# THIS PROGRAM AUTOMATES WORD SEARCHES IN A SCHOOL-STYLE, RECTANGULAR 
# BLOCK OF LETTERS WITH WORDS BURIED IN THEM.  
#
# THE GOAL:
# TO FIND THE WORDS ALONG ROWS, COLUMNS, OR DIAGONALS, IN
# FORWARD OR REVERSE DIRECTIONS.  IT PRINTS THE CROSSWORD, HIGHLIGHTING
# THE WORDS IT FINDS.
#
# NOTE:  This is NOT related to the NY Times style 
#        crossword puzzles
##############################################################
#
# 
# EXAMPLE:
#
#   >> fileName = "xwpuzzle.txt"
#   >> xw = readXW(fileName)    
# 
# CROSSWORD:
#   S    A    P    I    N    D    E    N    O    E    L
#   C    A    D    E    A    U    X    I    N    B    H
#   L    J    O    N    E    I    G    E    O    O    O
#   O    O    J    S    A    B    O    T    E    U    U
#   C    U    O    R    C    U    O    R    L    G    A
#   H    E    Y    E    H    C    E    A    E    I    P
#   E    T    E    N    I    H    M    I    I    E    E
#   S    C    U    N    M    E    B    N    C    O    R
#   S    A    X    E    I    D    A    E    O    R    E
#   N    N    N    U    N    E    L    A    U    E    F
#   O    N    O    A    E    N    L    U    R    V    O
#   I    E    E    D    E    O    E    E    O    E    U
#   T    D    L    E    R    E    R    E    N    I    E
#   A    E    I    E    H    L    K    L    N    L    T
#   R    N    J    E    I    O    N    I    E    L    T
#   O    O    I    H    V    L    I    E    M    O    A
#   C    E    L    I    E    U    H    N    L    N    R
#   E    L    L    L    R    X    G    O    P    O    D
#   D    E    C    E    M    B    R    E    R    S    P
#   
#
# With one function, you can search (1 word at a time)
# and it will print the crossword with the search-word
# highlighted, as shown below:
#
#   >> searchXW(xw, "decorations");
# 
# CROSSWORD:
#   S    A    P    I    N    D    E    N    O    E    L
#   C    A    D    E    A    U    X    I    N    B    H
#   L    J    O    N    E    I    G    E    O    O    O
#   O    O    J    S    A    B    O    T    E    U    U
#   C    U    O    R    C    U    O    R    L    G    A
#   H    E    Y    E    H    C    E    A    E    I    P
#   E    T    E    N    I    H    M    I    I    E    E
#   S    C    U    N    M    E    B    N    C    O    R
#  (S)   A    X    E    I    D    A    E    O    R    E
#  (N)   N    N    U    N    E    L    A    U    E    F
#  (O)   N    O    A    E    N    L    U    R    V    O
#  (I)   E    E    D    E    O    E    E    O    E    U
#  (T)   D    L    E    R    E    R    E    N    I    E
#  (A)   E    I    E    H    L    K    L    N    L    T
#  (R)   N    J    E    I    O    N    I    E    L    T
#  (O)   O    I    H    V    L    I    E    M    O    A
#  (C)   E    L    I    E    U    H    N    L    N    R
#  (E)   L    L    L    R    X    G    O    P    O    D
#  (D)   E    C    E    M    B    R    E    R    S    P
#
#
#   >>  searchXW(xw, "pole");
#
# CROSSWORD:
#   S    A    P    I    N    D    E    N    O    E    L
#   C    A    D    E    A    U    X    I    N    B    H
#   L    J    O    N    E    I    G    E    O    O    O
#   O    O    J    S    A    B    O    T    E    U    U
#   C    U    O    R    C    U    O    R    L    G    A
#   H    E    Y    E    H    C    E    A    E    I    P
#   E    T    E    N    I    H    M    I    I    E    E
#   S    C    U    N    M    E    B    N    C    O    R
#   S    A    X    E    I    D    A    E    O    R    E
#   N    N    N    U    N    E    L    A    U    E    F
#   O    N    O    A    E    N    L    U    R    V    O
#   I    E    E    D    E    O    E    E    O    E    U
#   T    D    L    E    R    E    R    E    N    I    E
#   A    E    I    E    H    L    K    L    N    L    T
#   R    N    J    E    I    O    N    I    E    L    T
#   O    O    I    H    V    L    I   (E)   M    O    A
#   C    E    L    I    E    U    H    N   (L)   N    R
#   E    L    L    L    R    X    G    O    P   (O)   D
#   D    E    C    E    M    B    R    E    R    S   (P)
#   
##############################################################
import os
import numpy as np

workingDir = "C:\\Users\\Bart\\Documents\\Data_G\\Python\\Crossword\\"
os.chdir(workingDir)
from crossword import *


# This is a text file with all the letters in the crossword
fileName = "xwpuzzle.txt"
xw = readXW(fileName)    


# printXW(xw)

searchXW(xw, "decorations");
searchXW(xw, "decor");
searchXW(xw, "dec");
searchXW(xw, "bougie");
searchXW(xw, "couronne");
searchXW(xw, "cou");
searchXW(xw, "renne");
searchXW(xw, "cloches");
searchXW(xw, "neige");
searchXW(xw, "hiver");
searchXW(xw, "chiminee");

searchXW(xw, "saxeida");

(wordFound, rStart, cStart, direction) = searchXW(xw, "sabot")
(wordFound, rStart, cStart, direction) = searchXW(xw, "cannedeNoel")
(wordFound, rStart, cStart, direction) = searchXW(xw, "sapin de noel")
(wordFound, rStart, cStart, direction) = searchXW(xw, "saosc")
(wordFound, rStart, cStart, direction) = searchXW(xw, "cojero")
(wordFound, rStart, cStart, direction) = searchXW(xw, "houx")

searchXW(xw, "noel");
searchXW(xw, "pere noel");
searchXW(xw, "pere fouettard");
searchXW(xw, "reveillon");
searchXW(xw, "nord");
searchXW(xw, "emballer");

searchXW(xw, "");
searchXW(xw, "");



