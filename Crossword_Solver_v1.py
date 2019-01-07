
import os
import sys
import numpy as np

workingDir = "C:\\Users\\Bart\\Documents\\Data_G\\Python\\Kiera_Crossword\\"
os.chdir(workingDir)

from crossword import *

xw = np.array([     "sapinDENOEL",
                    "CADEAUXINBH",
                    "LJONEIGEOOO",
                    "OOJSABOTEUU",
                    "CUORCUORLGA",
                    "HEYEHCEAEIP",
                    "ETENIHMIIEE",
                    "SCUNMEBNCOR",
                    "SAXEIDAEORE",
                    "NNNUNELAUEF",
                    "ONOAENLURVO",
                    "IEEDEOEEOEU",
                    "TDLERERENIE",
                    "AEIEHLKLNLT",
                    "RNJEIONIELT",
                    "OOIHVLIEMOA",
                    "CELIEUHNLNR",
                    "ELLLRXGOPOD",
                    "DECEMBRERSP" ] )
                    

searchStr = "sabot"
(wordFound, rStart, cStart, direction) = searchXW(xw, searchStr)






# Search for words in the rows
(wordFound, rStart, cStart, direction) = searchRows(xw, "ION",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "SAPIN",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "NOEL",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "DECE",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "RERSP",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "HEYEHCEAEIP",  searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchRows(xw, "ABCDEFGHIJ",  searchReverse=False, showXW=True)        # DOES NOT EXIST IN THIS PUZZLE


# Search for words in the columns
(wordFound, rStart, cStart, direction) = searchCols(xw, "OJOY", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "SCLOCH", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "LHOUAP", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "TARDP", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "TAROCED", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "EXGOOEMBALLERKNIHGR", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchCols(xw, "ABCDEFGHIJ", searchReverse=False, showXW=True)        # DOES NOT EXIST IN THIS PUZZLE


# Search for words along the diagonals
(wordFound, rStart, cStart, direction) = searchDiag(xw, "SAOSC", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "PEEBOA", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "PEEBOAIOE", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "AIOE", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "OBO", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "SANA", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "TEJHEXR", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "EE", searchReverse=False, showXW=True)
(wordFound, rStart, cStart, direction) = searchDiag(xw, "ABCDEFGHIJ", searchReverse=False, showXW=True)        # DOES NOT EXIST IN THIS PUZZLE










# (rows,cols) = getSize(xw)

"""
indexMapping = np.array( [  [ 8,4,0,9,7,9,7],
                            [ 1,0,9,4,4,9,5],
                            [ 6,6,2,7,9,2,1] ] )
"""


(rowStr,r,c)  = getRowStr(xw,3)
(colStr,r,c)  = getColStr(xw,4)
(diagStr,r,c) = getDiagStr
idx = c4.find('EACH')

c4
revStr(c4)


r1 = getRowStr(xw,1)

printXW(xw, rStart=-1, cStart=-1, numChars=0, direction='down')
printXW(xw, rStart=1, cStart=1, numChars=5, direction='down')
printXW(xw, rStart=1, cStart=1, numChars=5, direction='across')
printXW(xw, rStart=1, cStart=1, numChars=5, direction='diag')


printXW(xw, rStart=4, cStart=4, numChars=5, direction='down')
printXW(xw, rStart=4, cStart=4, numChars=5, direction='across')
printXW(xw, rStart=4, cStart=4, numChars=5, direction='diag')


 
 
    




file = 'C:\\Users\\Bart\\Downloads\\20190105_140704.txt'                
# xw = np.loadtxt(file)


fh = open(file, "rt")
np.fromfile(fh, dtype=dt)
np.fromfile(fh, dtype=dt)


xw = np.loadtxt(file,dtype='str');
xw = np.loadtxt(file,dtype='|S1');
xw = np.loadtxt(file,dtype='char');

xw = np.genfromtxt(file, dtype='str')


import pandas as pd
# df = pd.read_csv(file,sep='\t')
df = pd.read_csv(file,sep='\t')



"""
xw2 = np.chararray( (rows,cols)) 
for r in range(rows):
    k = xw[r]
    for c in range(cols):
        xw2[r,c] = k[c]
"""
    













