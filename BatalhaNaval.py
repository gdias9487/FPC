def create_matrix(l, c):
    matrix = []
    for i in range(int(l)):
        line = []
        columns = input()
        for j in columns:
            line.append(j)
        matrix.append(line)
    return matrix

def shots(matrix):
    global nboat
    global lenght
    shots = int(input())
    for i in range(shots):
        line, column = input().split(' ')
        line = int(line) - 1
        column = int(column) - 1
        if matrix[line][column] == '.':
            pass
        elif matrix[line][column] == '#':
            matrix[line][column] = nboat
            len_boat(matrix,line,column)
            nboat +=1
            boats.append(lenght)
            lenght = 1
            clean_shot(len_boat(matrix, line, column), line, column)
        else:
            clean_shot(len_boat(matrix, line, column), line, column)


def clean_shot(matrix,l,c):
    boats[matrix[l][c]] -= 1
def len_boat(matrix, line, column):
    global nboat
    global lenght
    #abaixo
    if (line + 1 <= (len(matrix) - 1)) and (matrix[line+1][column] == '#'):
        matrix[line+1][column] = nboat
        lenght += 1
        len_boat(matrix, line+1, column)
    #acima
    if (line - 1 >= 0) and (matrix[line-1][column] == '#'):
        matrix[line-1][column] = nboat
        lenght += 1
        len_boat(matrix, line-1, column)

    #direita
    if (column + 1 <= (len(matrix[0]) - 1) and (matrix[line][column+1] == '#')):
        matrix[line][column + 1] = nboat
        lenght += 1
        len_boat(matrix, line, column+1)

    #esquerda
    if (column - 1 >= 0) and (matrix[line][column-1] == '#'):
        matrix[line][column - 1] = nboat
        lenght += 1
        len_boat(matrix, line, column - 1)

    else:
        return matrix

hits = 0
nboat= 0
lenght = 1
boats = []
n, m = input().split(' ')
shots(create_matrix(n, m))
for i in boats:
    if i == 0:
        hits+=1
print(hits)