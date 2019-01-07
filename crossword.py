

import numpy as np

#########################################################################################################
def readXW(fileName):
    """
    """
    
    # Read the lines of the crossword puzzle 
    fo = open(fileName)
    xwRawLines = fo.readlines()

    # Extract the lines into a cleaned list... removes newlines & spaces, and changes all text to UPPER CAPS
    xwList = []
    for L in xwRawLines:
        xwList.append( L.strip().replace(' ','').upper() )

    # Put all the cleaned words into a numpy array
    xw = np.array([])
    for L in xwList:
        xw = np.append(xw, L)
        
        
    print("\nCrossword Loaded...\n")
    printXW(xw)
    return xw
#########################################################################################################
def printXW(xw, rStart=-1, cStart=-1, numChars=0, direction='down'):
    """
    printXW(xw,  rStart=-1, cStart=-1, numChars=0, direction='down')
    
    Prints the MxN numpy array of crosword (XW) characters.
    
    ARGS:
        xw:         Nx1 array of equal-length strings containing the crossword chars
        rStart:     Starting row of the string to be highlighted;
                    Set to -1 to avoid highlighting words on the crossword.
        cStart:     Starting col of the string to be highlighted
                    Set to -1 to avoid highlighting words on the crossword.
        numChars:   Number of chars to highlight
        
        direction:  The direction of the chars to highlight, starting at (rStart,cStart)
        
        
    """

    ##########################################
    # FOR DEBUG ONLY
    ##########################################
    # rStart = -1
    # cStart = -1
    # numChars = 0
    # direction = 'down'
    # 
    # rStart = 1
    # cStart = 2
    # numChars = 5
    # direction = 'across'
    ##########################################

    # print("\nHighlighting, starting at ({0},{1}), {2}, {3} chars total\n".format(rStart, cStart, direction, numChars))

    # For the 'diagup' direction, we must start at the END of the word and go backward.... because
    # we print the crossword from top to bottom.
    if ( direction == 'diagup' ):
        rStart = rStart - numChars + 1
        cStart = cStart + numChars - 1
    
    if ( rStart <= 0 ):
        cStart = -1
        numChars = 0

    if ( cStart <= 0 ):
        rStart = -1
        numChars = 0

    if ( numChars <= 0 ):
        rStart = -1
        numChars = 0

    # Switch from 1s indexing to 0s based indexing
    if (rStart >= 0):
        rStart -= 1
    if (cStart >= 0):
        cStart -= 1

    (rows,cols) = getSize(xw)
    
    # Tracks the row,col index of the next char to be highlighted
    rIdx=-1
    cIdx=-1
    
    if ( rStart >= 0 ):
        rIdx = rStart
    if ( cStart >= 0 ):
        cIdx = cStart
    
    numCharsFound = 0
    
    print("\n\n")
    print("CROSSWORD:", end='', flush=True)
    for r in range(rows):
        print("\n", end='', flush=True)
        for c in range(cols):
            ch = xw[r]
            ch = ch[c]
            
            foundChar = False
            if ( r == rIdx  and  c == cIdx and  numCharsFound < numChars):
                print( " ({0}) ".format(ch), end='', flush=True)
                foundChar = True
                numCharsFound += 1
            else:
                print( "  {0}  ".format(ch), end='', flush=True)
                
            # If we printed a string char this go round, then advance the 
            # rIdx and/or cIdx to the next char to be printed
            if ( foundChar is True ):
                foundDir = False
                if ( direction == 'down' ):
                    rIdx += 1       # The next char is 1 row down
                    foundDir = True
                if ( direction == 'across' ):
                    cIdx += 1       # The next char is the col to the right
                    foundDir = True
                if ( direction == 'diagdown' ):
                    rIdx += 1       # The next char is 1 row down
                    cIdx += 1       # The next char is the col to the right
                    foundDir = True
                if ( direction == 'diagup' ):
                    rIdx += 1       # The next char is 1 row down
                    cIdx -= 1       # The next char is the col to the left, since we started at the END of the specified (r,c) + numChars position
                    foundDir = True

                if ( foundDir is False ):
                    raise ValueError("\n\nERROR in crossword 'printXW': \n\tUnrecognized direction, '{0}'\n\n".format(direction))

    print("\n")

    return
#########################################################################################################
def searchXW(xw, searchStr, searchReverse=True):
    """
    (wordFound, rStart, cStart, direction) = searchXW(xw, searchStr, searchReverse=True)
    
    This is the primary search function you use to search the crossword puzzle.
    It searches across rows, down columns, diagonals moving down & right  (\)
    and diagonals moving up and right (/).
    
    ARGUMENTS:
        xw:     Mx1 numpy array of strings, each of which contains 1 row of letters for the crossword.
                Use function "readXW" to load it from a text file
 searchStr:     Any search string
 searchReverse: Boolean.  If False, it searches rows and diagonals left-to-right,  and it
                          searches columns top-to-bottom only
                          If True, it searches BOTH forward and reverse direction text.                          
    
    
    See Also:
        Use function "readXW" to read the crossword from a text file (a block of letters)
    """
    
    #  Initialize return values
    wordFound = False
    rStart = -1
    cStart = -1
    direction = ''
    
    # Make the search string all CAPS, removing leading whitespace, removing all spaces
    searchStr = searchStr.upper().strip().replace(' ','')

    # Make the XW puzzle all CAPS
    (rows,cols) = getSize(xw)    
    for k in range(rows):
        xw[k] = xw[k].upper()


    # Search for words in the rows
    (wordFound, rStart, cStart, direction) = searchRows(xw, searchStr,  searchReverse=False, showXW=True)

    if( wordFound ):
        return (wordFound, rStart, cStart, direction)
                

    # Search for words in the columns
    (wordFound, rStart, cStart, direction) = searchCols(xw, searchStr, searchReverse=False, showXW=True)

    if( wordFound ):
        return (wordFound, rStart, cStart, direction)

    # Search for words along the diagonals that move down & to the right,  like "\"
    (wordFound, rStart, cStart, direction) = searchDiagDown(xw, searchStr, searchReverse=False, showXW=True)

    if( wordFound ):
        return (wordFound, rStart, cStart, direction)

    # Search for words along the diagonals that move up & to the right,  like "/"
    (wordFound, rStart, cStart, direction) = searchDiagUp(xw, searchStr, searchReverse=False, showXW=True)

    if( wordFound ):
        return (wordFound, rStart, cStart, direction)


    # If we also search in reverse
    if ( searchReverse is True ):
        # Search for words in the rows
        (wordFound, rStart, cStart, direction) = searchRows(xw, searchStr,  searchReverse=True, showXW=True)

        if( wordFound ):
            return (wordFound, rStart, cStart, direction)
                    

        # Search for words in the columns
        (wordFound, rStart, cStart, direction) = searchCols(xw, searchStr, searchReverse=True, showXW=True)

        if( wordFound ):
            return (wordFound, rStart, cStart, direction)

        # Search for words along the diagonals that move down & to the right,  like "\"
        (wordFound, rStart, cStart, direction) = searchDiagDown(xw, searchStr, searchReverse=True, showXW=True)

        if( wordFound ):
            return (wordFound, rStart, cStart, direction)

        # Search for words along the diagonals that move up & to the right,  like "/"
        (wordFound, rStart, cStart, direction) = searchDiagUp(xw, searchStr, searchReverse=True, showXW=True)

        if( wordFound ):
            return (wordFound, rStart, cStart, direction)
            
    if( not wordFound ):
        print("\n\nSearch word '{0}' not found\n".format(searchStr))
    
    return (wordFound, rStart, cStart, direction)
#########################################################################################################  
def searchRows(xw, searchStr, searchReverse=False, showXW=False):
    """
    (wordFound, rStart, cStart, direction) = searchRows(xw, searchStr, searchReverse=False, showXW=False)
    
    Searchs all the rows of "xw" (MxN array of chars) and 
    if it's found, it prints the crossword puzzle and
    highlights the word it found.
    
 searchReverse: Boolean.  If False, it searches in the FORWARD DIRECTION ONLY;  
                          i.e. it searches rows left-to-right,  
                          If True, it searches in the REVERSE DIRECTION ONLY;  
    
    It returns a 4-tuple:
        wordFound:   boolean, indicating whether the word was found
        rStart:      1s based index of the starting row where the word was found
        cStart:      1s based index of the starting col where the word was found
        direction:   Direction string, either 'down' or 'up', indicating whether the word was reversed
        
    
    """
    
    # searchStr = "MEB"
    # searchStr = "SAPIN"
    
    if ( searchReverse is True ):
        searchStr = reverseStr(searchStr)
    
    (rows,cols) = getSize(xw)
    
    c      = -1
    rStart = -1
    cStart = -1
    numChars = 0
    direction='across'
    for r in range(rows):
        (rowStr,rx,cx) = getRowStr(xw,r+1)
        idx = rowStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current column matches the index returned by .find
            c = idx
            # print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r,c,rowStr))
            rStart = r+1
            cStart = c+1
            numChars = len(searchStr)
            if ( showXW is True ):         
                printXW(xw, rStart, cStart, numChars, direction)
            break
        
        
    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
    else:
        wordFound = False
    
    
    return  (wordFound, rStart, cStart, direction)
#########################################################################################################
def searchCols(xw, searchStr, searchReverse=False, showXW=False):
    """
    (wordFound, rStart, cStart, direction) = searchCols(xw, searchStr, searchReverse=False, showXW=False)
    
    Searchs all the cols of "xw" (MxN array of chars) and 
    if it's found, it prints the crossword puzzle and
    highlights the word it found.
    
 searchReverse: Boolean.  If False, it searches in the FORWARD DIRECTION ONLY;  
                          i.e. it searches columns top-to-bottom  
                          If True, it searches in the REVERSE DIRECTION ONLY;  
    
    It returns a 4-tuple:
        wordFound:   boolean, indicating whether the word was found
        rStart:      1s based index of the starting row where the word was found
        cStart:      1s based index of the starting col where the word was found
        direction:   Direction string, either 'down' or 'up', indicating whether the word was reversed
    
    """
    
    # searchStr = "OJOY"
    
    if ( searchReverse is True ):
        searchStr = reverseStr(searchStr)
    
    (rows,cols) = getSize(xw)
    
    c = -1
    rStart = -1
    cStart = -1
    numChars = 0
    direction='down'
    
    for c in range(cols):
        (colStr,rx,cx) = getColStr(xw,c+1)
        idx = colStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current column matches the index returned by .find
            r = idx
            # print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r,c,colStr))
            rStart = r+1
            cStart = c+1
            numChars = len(searchStr)
            if ( showXW is True ):         
                printXW(xw, rStart, cStart, numChars, direction)
            break
        
        
    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
    else:
        wordFound = False
    
    
    return  (wordFound, rStart, cStart, direction)
#########################################################################################################
def searchDiagDown(xw, searchStr, searchReverse=False, showXW=False):
    """
    (wordFound, rStart, cStart, direction) = searchDiagDown(xw, searchStr, searchReverse=False, showXW=False)
    
    Searchs all the left-to-right DOWNWARD diagonals of "xw" (MxN array of chars) and 
    if it's found, it prints the crossword puzzle and
    highlights the word it found.
    
 searchReverse: Boolean.  If False, it searches in the FORWARD DIRECTION ONLY;  
                          i.e. it searches diagonals left-to-right, in the downward direction.  
                          If True, it searches in the REVERSE DIRECTION ONLY;  
    
    It returns a 4-tuple:
        wordFound:   boolean, indicating whether the word was found
        rStart:      1s based index of the starting row where the word was found
        cStart:      1s based index of the starting col where the word was found
        direction:   Direction string, 'diagdown', indicating whether the word was reversed
    
    """
    
    if ( searchReverse is True ):
        searchStr = reverseStr(searchStr)
    
    # searchStr = "AIOE"
    
    (rows,cols) = getSize(xw)

    rStart = -1
    cStart = -1
    numChars = 0
    direction='diagdown'

    # Search the diagonals attached to the top row
    r = 0
    for c in range(cols):
        (diagStr,rx,cx) = getDiagStrDown(xw, r+1, c+1)
        # print(diagStr)
                
        idx = diagStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current diagonal matches the index returned by .find
            # print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r+idx,c+idx,diagStr))
            rStart = 1+idx
            cStart = c+1+idx
            numChars = len(searchStr)
            if ( showXW is True ):
                printXW(xw, rStart=rStart, cStart=cStart, numChars=numChars, direction=direction)
                
            break

        
    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
        return (wordFound, rStart, cStart, direction)
    else:
        wordFound = False



    # Search the diagonals attached to the first column
    c = 0
    for r in range(rows):
        (diagStr,rx,cx) = getDiagStrDown(xw, r+1, c+1)
        # print(diagStr)
                
        idx = diagStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current diagonal matches the index returned by .find
            print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r,c,diagStr))
            rStart = r+1+idx
            cStart = 1+idx
            numChars = len(searchStr)
            if ( showXW is True ):
                printXW(xw, rStart=rStart, cStart=cStart, numChars=numChars, direction=direction)
                
            break


        
    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
        return (wordFound, rStart, cStart, direction)
    else:
        wordFound = False
    
    
    return  (wordFound, rStart, cStart, direction)
#########################################################################################################
def searchDiagUp(xw, searchStr, searchReverse=False, showXW=False):
    """
    (wordFound, rStart, cStart, direction) = searchDiagUp(xw, searchStr, searchReverse=False, showXW=False)
    
    Searchs all the left-to-right UPWARD diagonals of "xw" (MxN array of chars) and 
    if it's found, it prints the crossword puzzle and
    highlights the word it found.
    
 searchReverse: Boolean.  If False, it searches in the FORWARD DIRECTION ONLY;  
                          i.e. it searches the diagonals left-to-right, in the upward direction.  
                          If True, it searches in the REVERSE DIRECTION ONLY;  
    
    It returns a 4-tuple:
        wordFound:   boolean, indicating whether the word was found
        rStart:      1s based index of the starting row where the word was found
        cStart:      1s based index of the starting col where the word was found
        direction:   Direction string, 'diagup', indicating whether the word was reversed
    
    """
    
    # searchStr = "AIOE"
    if ( searchReverse is True ):
        searchStr = reverseStr(searchStr)

    
    (rows,cols) = getSize(xw)

    rStart = -1
    cStart = -1
    numChars = 0
    direction='diagup'


    # Search the diagonals attached to the first column
    c = 0
    for r in range(rows):
        (diagStr,rx,cx) = getDiagStrUp(xw, r+1, c+1)
        # print(diagStr)
                
        idx = diagStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current diagonal matches the index returned by .find
            print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r,c,diagStr))
            rStart = r+1-idx
            cStart = 1+idx
            numChars = len(searchStr)
            if ( showXW is True ):
                printXW(xw, rStart=rStart, cStart=cStart, numChars=numChars, direction=direction)
                
            break


    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
        return (wordFound, rStart, cStart, direction)
    else:
        wordFound = False



    # Search the diagonals attached to the bottom row
    r = rows-1
    for c in range(cols):
        (diagStr,rx,cx) = getDiagStrUp(xw, r+1, c+1)
        # print(diagStr)
                
        idx = diagStr.find(searchStr)
        if ( idx >= 0 ):            # IF .find returned a match AND the current diagonal matches the index returned by .find
            # print("Found search string '{0}' in (row,col) = ({1},{2}):   {3}\n".format(searchStr, r+idx,c+idx,diagStr))
            rStart = 1+idx
            cStart = c+1+idx
            numChars = len(searchStr)
            if ( showXW is True ):
                printXW(xw, rStart=rStart, cStart=cStart, numChars=numChars, direction=direction)
                
            break

        
    if (rStart > 0  and  cStart > 0  and  numChars > 0):
        wordFound = True
        return (wordFound, rStart, cStart, direction)
    else:
        wordFound = False


    return  (wordFound, rStart, cStart, direction)
#########################################################################################################
def getSize(xw):
    """
    (rows,cols) = getSize(xw)
    
    Gets the # rows & cols of chars in this crossword
    
    """
    rows = xw.shape[0]
    rowStr = xw[0]
    cols = len(rowStr)
    return (rows,cols)    
#########################################################################################################
def reverseStr(txtStr):
    """
    reversedStr = reverseStr(txtStr)
    
    This reverses the order of chars in a string
    """
    return txtStr[::-1]
#########################################################################################################
def getDiagStrDown(xw,r,c, searchReverse=False):
    """
    (diagStr,r,c) = getDiagStrDown(xw,r,c, searchReverse=False)
    
    Extract char string from a diagonal of "xw", the numpy array of chars;
    The diagonal of chars starts at (r,c), using 1s based indexing,
    and extends as far as possible down and right.
    
    It returns a 3-tuple containing the diagonal string of chars and the (row,col) 
    of the first char location.

    ARGS:
    xw is a 2D numpy array of characters.
    r is a 1s based index (r >= 1) of the row to extract.   

    From the Nx1 numpy array of strings, extract string diagonals,
    STARTING at position (r,c) and moving in the LOWER-RIGHT (LR) direction
    """
    
    r    -= 1
    c    -= 1
    
    rowStr = getRowStr(xw, 1)

    (rows,cols) = getSize(xw)

    diagStr = ""
    ridx = r
    cidx = c
    for idx in range(5000):     # Just a loop... the index is not used;  ridx and cidx are they main indices used    
        (rowStr,rx,cx) = getRowStr(xw, ridx+1)
        diagStr += rowStr[cidx]
        if ( ridx >= rows-1):
            break
        if ( cidx >= cols-1):
            break
        # if ( ridx <= 0 ):
        #     break
        # if ( cidx <= 0):
        #     break
            
        ridx += 1       # Move DOWN a row
        cidx += 1       # Next column to the right
            
    r += 1          
    c += 1
    return (diagStr,r,c)       
#########################################################################################################
def getDiagStrUp(xw,r,c, searchReverse=False):
    """
    (diagStr,r,c) = getDiagStrUp(xw,r,c, searchReverse=False)
    
    Extract char string from a diagonal of "xw", the numpy array of chars;
    The diagonal of chars starts at (r,c), using 1s based indexing,
    and extends as far as possible up and right.
    
    It returns a 3-tuple containing the diagonal string of chars and the (row,col) 
    of the first char location.

    ARGS:
    xw is a 2D numpy array of characters.
    r is a 1s based index (r >= 1) of the row to extract.   

    From the Nx1 numpy array of strings, extract string diagonals,
    STARTING at position (r,c) and moving in the LOWER-RIGHT (LR) direction
    """
    
    r    -= 1
    c    -= 1
    
    rowStr = getRowStr(xw, 1)

    (rows,cols) = getSize(xw)

    diagStr = ""
    ridx = r
    cidx = c
    for idx in range(1000):     # Just a loop... the index is not used;  ridx and cidx are they main indices used    
        (rowStr,rx,cx) = getRowStr(xw, ridx+1)
        diagStr += rowStr[cidx]
        # if ( ridx >= rows-1 ):
        #     break
        if ( cidx >= cols-1 ):
            break
        if ( ridx <= 0 ):
            break
        # if ( cidx <= 0 ):
        #     break
            
        ridx -= 1       # Move UP a row
        cidx += 1       # Next column to the right
            
    r += 1
    c += 1
    return (diagStr,r,c)       
#########################################################################################################
def getRowStr(xw, r):
    """
    (rowStr,r,c) = getRowStr(xw, r)
    
    Extract char string from row r of "xw", the numpy array of chars;
    It returns a 3-tuple containing the row string of chars and the (row,col) 
    of the first char location.

    ARGS:
    xw is a 2D numpy array of characters.
    r is a 1s based index (r >= 1) of the row to extract.   
    """

    r -= 1
    rowStr = ""
    rowStr = str(xw[r])
    
    c=1
    r+=1    # back to 1s based indexing
    return (rowStr,r,c)
#########################################################################################################    
def getColStr(xw, c):
    """
    (colStr,r,c) = getRowStr(xw, c)
    Extract char string from col c of "xw", the numpy array of chars;
    It returns a 3-tuple containing the col string of chars and the (row,col) 
    of the first char location.

    ARGS:
    xw is a 2D numpy array of characters.
    c is a 1s based index (c >= 1) of the column to extract.   
    
        
    """

    c -= 1          
    colStr = ""
    
    rows=xw.shape[0]
    
    for r in range(rows):
        rowStr = str(xw[r])
        colStr += rowStr[c]
    
    r=1
    c+= 1       # back to 1s based indexing
    return (colStr, r, c)
#########################################################################################################
