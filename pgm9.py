import errno, sys  # for proper error handling


def GetInlineMatrixIndex(matrixList, matrixSideLength, row, col):
    # validate the integrity of the received data to ensure row col values are in range
    if ( ((row > 0) and (row <= matrixSideLength)) and ((col > 0) and (col <= matrixSideLength))):
        # 1   2  3  4     rowNum(1) -->   row1 = 1    = 1                                = [(rowNum(1) - 1) * matrixSideLength] + 1  == 1
        # 5   6  7  8     rowNum(2) -->   row2 = 5    = row1 + 4      = 1 + 4            = [(rowNum(2) - 1) * matrixSideLength] + 1  == 5
        # 9  10 11 12     rowNum(3) -->   row3 = 9    = row2 + 4      = 1 + 4 + 4        = [(rowNum(3) - 1) * matrixSideLength] + 1  == 9
        # 13 14 15 16     rowNum(4) -->   row4 = 13   = row3 + 4      = 1 + 4 + 4 + 4    = [(rowNum(4) - 1) * matrixSideLength] + 1  == 13

        # r = ((row - 1) * matrixSideLength) + 1
        # r = r  - 1  # matracies are zero relative
        # c = col - 1 # matracies are zer0 relative
        # index = r + c
        #
        # readableFormula = ((((((row - 1) * matrixSideLength) + 1) - 1) + col) - 1)
        # refinedFormula  = ((((row - 1) * matrixSideLength) + col) - 1)
        return ((((row - 1) * matrixSideLength) + col) - 1)
    else:
        print('ERROR: ({},{}) is outside of the matrix range, invalid index.'.format(row,col))
        sys.exit(errno.EPERM) # operation not permitted

def GetInlineMatrixIndexValue(matrixList, matrixSideLength, row, col):
    return matrixList[GetInlineMatrixIndex(matrixList, matrixSideLength, row, col)]
    

def SetInlineMatrixIndexValue(matrixList, matrixSideLength, row, col, value):
    matrixList[GetInlineMatrixIndex(matrixList, matrixSideLength, row, col)] = value




# read the lines from TestData.txt
lines = [line.rstrip('\n') for line in open('C:\Users\LANIERK\MyFiles\PythonTraining\WSU\TestData.txt')]

# remove all white space, commas, and braces
matrixData = lines[1].replace(',','').replace(' ','').replace('{', '').replace('}', '')

# validate the integrity of the NxN matrix
if (len(matrixData)%4 is not 0):
    print('ERROR: NxN matrix was not provided, invalid matrix.')
    sys.exit(errno.EPERM) # operation not permitted

# inline NxN maytracies can be evenly divided by 4
matrixSideLength = len(matrixData)/4 

# change the string to a list so individual indicies can be manipulated
matrix = list(matrixData)

# print the matrix contents before manipulation
print('matrix = {}'.format(matrix))

# where row and col are in the set of Natural numbers and both are <= matrixSideLength
row = 4
col = 2

# print the current value of (row,col)
print('({},{}) = {}'.format(row,col,GetInlineMatrixIndexValue(matrix, matrixSideLength, row, col)))

# set the new value of (row,col)
SetInlineMatrixIndexValue(matrix, matrixSideLength, row, col, value='X')

# print the new value of (row,col)
print('({},{}) = {}'.format(row,col,GetInlineMatrixIndexValue(matrix, matrixSideLength, row, col)))

# print the matrix contents after manipulation
print('matrix = {}'.format(matrix))