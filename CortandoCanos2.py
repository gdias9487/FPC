def greater(a, b):  # Função máximo
    return (a + b + absolute(a - b)) // 2


def absolute(a):
    if a > 0:
        return a
    else:
        return -a


def matrix(c, n):  # Gera a matriz para encontrar o resultado.
    matrix = [['*'] + [int(x) for x in range(c + 1)]]
    for i in range(n + 1):
        matrix.append([i] + [0] * (c + 1))

    return matrix


def knapsack(c, n, m, p):  # Compara as células da matriz utilizando a lógica do problema da mochila.
    for i in range(2, n + 2):
        for j in range(2, c + 2):
            if int(p[i - 2][0]) > m[0][j]:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = greater(m[i - 1][j], m[i][j - int(p[i - 2][0])] + int(p[i - 2][1]))

    return m[-1][-1]


n, c = [int(i) for i in input().split()]
pipes = [(input().split()) for x in range(n)]
matrix = matrix(c, n)
print(knapsack(c, n, matrix, pipes))