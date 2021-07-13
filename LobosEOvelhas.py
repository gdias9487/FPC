import sys
sys.setrecursionlimit(10000)

def create_matrix(l, c):
    matrix = []
    for i in range(int(l)):
        line = []
        columns = input()
        for j in columns:
            line.append(j)
        matrix.append(line)
    return matrix

def run_codes(matrix, l, c):
    global wolves
    global sheeps
    global lobos
    global ovelhas
    for line in range(l):
        for column in range(c):
            sheeps = 0
            wolves = 0
            if matrix[line][column] == '.':
                matrix[line][column] = '&'
                find(matrix,line,column)
                if wolves >= sheeps:
                    sheeps = 0
                    lobos += wolves
                else:
                    wolves = 0
                    ovelhas += sheeps
            elif matrix[line][column] == 'k':
                matrix[line][column] = '&'
                sheeps += 1
                find(matrix, line, column)
                if wolves >= sheeps:
                    sheeps = 0
                    lobos += wolves
                else:
                    wolves = 0
                    ovelhas += sheeps
            elif matrix[line][column] == 'v':
                matrix[line][column] = '&'
                wolves += 1
                find(matrix, line, column)
                if wolves >= sheeps:
                    sheeps = 0
                    lobos += wolves
                else:
                    wolves = 0
                    ovelhas += sheeps

def find(matrix, line,column):
    global l
    global c
    global wolves
    global sheeps
    if (line + 1 <= (l - 1)) and (matrix[line+1][column] == '.'):
        matrix[line+1][column] = '&'
        find(matrix, line+1, column)

    if (line - 1 >= 0) and (matrix[line-1][column] == '.'):
        matrix[line-1][column] = '&'
        find(matrix, line-1, column)

    if (column + 1 <= (c - 1) and (matrix[line][column+1] == '.')):
        matrix[line][column + 1] = '&'
        find(matrix, line, column+1)

    if (column - 1 >= 0) and (matrix[line][column-1] == '.'):
        matrix[line][column - 1] = '&'
        find(matrix, line, column - 1)

    if (line + 1 <= (l - 1)) and (matrix[line+1][column] == 'k'):
        matrix[line+1][column] = '&'
        sheeps += 1
        find(matrix, line+1, column)

    if (line - 1 >= 0) and (matrix[line-1][column] == 'k'):
        matrix[line-1][column] = '&'
        sheeps += 1
        find(matrix, line-1, column)

    if (column + 1 <= (c - 1) and (matrix[line][column+1] == 'k')):
        matrix[line][column + 1] = '&'
        sheeps += 1
        find(matrix, line, column+1)

    if (column - 1 >= 0) and (matrix[line][column-1] == 'k'):
        matrix[line][column - 1] = '&'
        sheeps += 1
        find(matrix, line, column - 1)

    if (line + 1 <= (l - 1)) and (matrix[line+1][column] == 'v'):
        matrix[line+1][column] = '&'
        wolves += 1
        find(matrix, line+1, column)

    if (line - 1 >= 0) and (matrix[line-1][column] == 'v'):
        matrix[line-1][column] = '&'
        wolves += 1
        find(matrix, line-1, column)

    if (column + 1 <= (c - 1) and (matrix[line][column+1] == 'v')):
        matrix[line][column + 1] = '&'
        wolves += 1
        find(matrix, line, column+1)

    if (column - 1 >= 0) and (matrix[line][column-1] == 'v'):
        matrix[line][column - 1] = '&'
        wolves += 1
        find(matrix, line, column - 1)

    else:
        return


sheeps = 0
wolves = 0
lobos = 0
ovelhas = 0
l,c = input().split()
l,c = int(l),int(c)
run_codes(create_matrix(l,c),l,c)
print(ovelhas, lobos)