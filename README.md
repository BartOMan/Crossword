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
