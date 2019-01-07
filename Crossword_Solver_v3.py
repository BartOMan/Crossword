
import os
import sys
import numpy as np

workingDir = "C:\\Users\\Bart\\Documents\\Data_G\\Python\\Crossword\\"
os.chdir(workingDir)
from crossword import *



fileName = "xwpuzzle.txt"
xw = readXW(fileName)    
# printXW(xw)


vocabWords = [ ]
# "sapin de noci"
# "cannedeNoel"        
# "sapin de noci"

(wordFound, rStart, cStart, direction) = searchXW(xw, "sabot")
(wordFound, rStart, cStart, direction) = searchXW(xw, "cannedeNoel")
(wordFound, rStart, cStart, direction) = searchXW(xw, "sapin de noel")
(wordFound, rStart, cStart, direction) = searchXW(xw, "saosc")
(wordFound, rStart, cStart, direction) = searchXW(xw, "cojero")
(wordFound, rStart, cStart, direction) = searchXW(xw, "houx")


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


searchXW(xw, "noel");
searchXW(xw, "pere noel");
searchXW(xw, "pere fouettard");
searchXW(xw, "reveillon");
searchXW(xw, "nord");
searchXW(xw, "emballer");

searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");
searchXW(xw, "");





