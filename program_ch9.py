import errno, sys  # for proper error handling
import math        # to use sqrt() to find the side length of a NxN matrix



def GetInlineMatrixAsList(strFilePath):
    # change the string of matrix data into a list so individual matrix indicies can be manipulated
    return list(GetInlineMatrxDataFromFile(strFilePath))


def GetInlineMatrxDataFromFile(strFilePath):
    # read the lines from TestData.txt
    lines = [line.rstrip('\n') for line in open(strFilePath)]
    # print the original condition of the in-line matrix
    print(lines[1])
    # remove all white space, commas, and braces
    matrixData = lines[1].replace(',','').replace(' ','').replace('{', '').replace('}', '')
    
    # if the length of the inline matrix is < 4 exit the program, or, 
    # if the length of the inline matrix does not have a perfect square root
    # then exit the program
    if  (((len(matrixData) < 4) or (math.sqrt(len(matrixData)) - int(math.sqrt(len(matrixData)))) != 0)):
        print('ERROR: NxN matrix of at least 2x2, read inline as {{0, 0}, {0, 0}} was not provided, invalid matrix.')
        # operation not permitted
        sys.exit(errno.EPERM)
    return matrixData


def GetInlineMatrixIndexValue(listMatrix, row, col):
    return listMatrix[GetInlineMatrixIndex(listMatrix, row, col)]
    

def SetInlineMatrixIndexValue(listMatrix, row, col, newValue):
    listMatrix[GetInlineMatrixIndex(listMatrix, row, col)] = newValue


def GetInlineMatrixIndex(listMatrix, row, col):
    # ensure the the length of the inline matrix has a perfect square root
    if ((math.sqrt(len(listMatrix)) - int(math.sqrt(len(listMatrix)))) == 0):

        matrixSideLength = int(math.sqrt(len(matrix)))

        # validate the integrity of the received data to ensure row col values are in range of the side length of the matrix
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
    else:
        print('ERROR: {}, is not a proper side length for an NxN matrix, invalid matrix.'.format(row,col))
        sys.exit(errno.EPERM) # operation not permitted


def PrintMatrix(listMatrix, boolPrintInline):
    print('\n')
    
    if(boolPrintInline):
        print('inlineMatrix = {}'.format(listMatrix))
    else:
        matrixSideLength = int(math.sqrt(len(matrix)))
        
        for row in range(1, matrixSideLength + 1):
            strRow = ""
            
            for col in range(1, matrixSideLength + 1):
                
                if (col == matrixSideLength):
                    strRow = strRow + GetInlineMatrixIndexValue(matrix, row, col)
                else:
                    strRow = strRow + GetInlineMatrixIndexValue(matrix, row, col) + ' '
            
            print(strRow)
    
    print('\n')

def ReturnMatrix(listMatrix):
    
    matrixSideLength = int(math.sqrt(len(matrix)))
    tempStr = ""

    for row in range(1, matrixSideLength + 1):
        strRow = "{"
            
        for col in range(1, matrixSideLength + 1):
            if ((row == (matrixSideLength)) and (col == matrixSideLength)):
                strRow = strRow + GetInlineMatrixIndexValue(matrix, row, col) + '}'
            elif (col == matrixSideLength):
                strRow = strRow + GetInlineMatrixIndexValue(matrix, row, col) + '},'
            else:
                strRow = strRow + GetInlineMatrixIndexValue(matrix, row, col) + ', '

        tempStr = tempStr + strRow
    
    tempStr = '{' + tempStr + '}'
    
    return tempStr


def PrintMatrixValue(listMatrix, row, col):
    print('({},{}) = {}'.format(row,col,GetInlineMatrixIndexValue(matrix, row, col)))


def BoolIsReflexive(listMatrix):
    charOne = '1'
    matrixSideLength = int(math.sqrt(len(listMatrix)))
    for i in range(1, (matrixSideLength + 1)):
        if (charOne != GetInlineMatrixIndexValue(listMatrix, i, i)):
            return False
    
    return True

def BoolIsSymmetric(listMatrix):
    matrixSideLength = int(math.sqrt(len(listMatrix)))

    for row in range(1, (matrixSideLength + 1)):
        for col in range(1, (matrixSideLength + 1)):
            a = GetInlineMatrixIndexValue(listMatrix, row, col)
            b = GetInlineMatrixIndexValue(listMatrix, col, row)
            
            if ( a != b):
                return False
    
    return True

def MakeReflexiveMatrix(listMatrix):
    matrixSideLength = int(math.sqrt(len(listMatrix)))

    for i in range(1, (matrixSideLength + 1)):
        SetInlineMatrixIndexValue(listMatrix, i, i, '1')

def MakeSymmetricMatrix(listMatrix):
    matrixSideLength - int(math.sqrt(len(listMatrix)))

    for row in range(1, (matrixSideLength + 1)):
        for col in range(1, (matrixSideLenght + 1)):
            a = GetInlineMatrixIndexValue(listMatrix, row, col)
            b = GetInlineMatrixIndexValue(listMatrix, col, row)

            if ((a == '1') or (b == '1')):
                SetInlineMatrixIndexValue(listMatrix, row, col, '1')
                SetInlineMatrixIndexValue(listMatrix, col, row, '1')







# read matrix data from file, return matrix as a pythoic list
matrix = GetInlineMatrixAsList('TestData.txt')


# print the matrix contents before manipulation
PrintMatrix(matrix, boolPrintInline=False)

# check if matrix ia reflexive
if (BoolIsReflexive(matrix)):
    print('Matrix is reflexive')
else:
    print('Matrix is not reflexive')

# check if matrix is symmetric
if (BoolIsSymmetric(matrix)):
    print('Matrix is symmetric')
else:
    print('Matrix is not symmetric')
print('------------')


MakeReflexiveMatrix(matrix)

PrintMatrix(matrix, boolPrintInline=False)

# check if matrix ia reflexive
if (BoolIsReflexive(matrix)):
    print('Matrix is reflexive')
else:
    print('Matrix is not reflexive')

# check if matrix is symmetric
if (BoolIsSymmetric(matrix)):
    print('Matrix is symmetric')
else:
    print('Matrix is not symmetric')
print('------------')



print(ReturnMatrix(matrix))
# PrintMatrix(matrix, boolPrintInline=False)

# # Note row and col are in the set of Natural numbers and both are <= matrixSideLength
# row = 2
# col = 2

# # print the current value of (row,col)
# PrintMatrixValue(matrix, row, col)

# # set the new value of (row, col)
# SetInlineMatrixIndexValue(matrix, row, col, newValue='X')

# # print the new value of (row, col)
# PrintMatrixValue(matrix, row, col)

# # print the matrix contents after manipulation
# PrintMatrix(matrix, boolPrintInline=False)

# # check if matrix ia reflexive
# if (BoolIsReflexive(matrix)):
#     print('Matrix is reflexive')
# else:
#     print('Matrix is not reflexive')

# # check if matrix is symmetric
# if (BoolIsSymmetric(matrix)):
#     print('Matrix is symmetric')
# else:
#     print('Matrix is not symmetric')
# print('------------')

# print('------------')
# PrintMatrix(matrix, boolPrintInline=False)


# # set the new value of (row, col)
# SetInlineMatrixIndexValue(matrix, row=1, col=2, newValue='X')

# # check if matrix ia reflexive
# if (BoolIsReflexive(matrix)):
#     print('Matrix is reflexive')
# else:
#     print('Matrix is not reflexive')

# # check if matrix is symmetric
# if (BoolIsSymmetric(matrix)):
#     print('Matrix is symmetric')
# else:
#     print('Matrix is not symmetric')
# print('------------')

# print('------------')
# PrintMatrix(matrix, boolPrintInline=False)