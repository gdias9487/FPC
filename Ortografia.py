def less(a, b):  # Resubmissão com a função mínimo implementada.
    return (a + b - absolute(a - b)) // 2


def absolute(a):
    if a > 0:
        return a
    else:
        return -a


def levenshtein(dic, comp):
    deletions = absolute(len(dic) - len(comp))  # Verifica a quantidade de inserções ou deleções necessárias.
    if deletions < 3:
        matrix = [[int(x) for x in range(len(dic) + 1)]]  # Gera as duas primeiras
        # linhas da matriz
        for i, c in enumerate(comp):
            matrix.append([i + 1] + [0] * (len(dic)))  # Gera as colunas da matriz, com as letras da segunda
            # palavra
        for j in (range(1, len(dic) + 1)):
            for i in (range(1, len(comp) + 1)):
                if dic[j - 1] == comp[i - 1]:
                    c = 0
                else:
                    c = 1
                matrix[i][j] = less(less(matrix[i - 1][j - 1] + c, matrix[i - 1][j] + 1), matrix[i][j - 1] + 1)

        return matrix[-1][-1]
    return deletions


dic, entry = [int(i) for i in input().split()]
dictionary = *[input() for i in range(dic)],  # A sintaxe "*[...]," pode ser usada para converter listas em tuplas
comparison = *[input() for i in range(entry)],
out = ''
for i in range(entry):
    for j in range(dic):
        if levenshtein(dictionary[j], comparison[i]) < 3:
            out += dictionary[j] + ' '
    print(out)
    out = ''
