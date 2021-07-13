def get_medals_info(c, m):
    matrix = []
    for i in range(c):
        matrix.append([i + 1, 0, 0, 0])
    for i in range(m):
        gold, silver, bronze = [int(x) for x in input().split()]
        for j in range(c):
            if matrix[j][0] == gold:
                matrix[j][1] += 1
            if matrix[j][0] == silver:
                matrix[j][2] += 1
            if matrix[j][0] == bronze:
                matrix[j][3] += 1
    for i in range(c):
        matrix[i] = tuple(matrix[i])
    return matrix


def medal_priority(matrix, i1, i2):
    less = []
    equal = []
    greater = []
    if len(matrix) > 1:
        if i1 < 4 and i2 < 5:
            pivot = matrix[0][i1]
            for i in range(len(matrix)):
                for x in matrix[i][i1:i2]:
                    if matrix[i][i1] == x:
                        if x > pivot:
                            greater.append(matrix[i])
                        elif x < pivot:
                            less.append(matrix[i])
                        else:
                            equal.append(matrix[i])

            return medal_priority(greater, i1, i2) + medal_priority(equal, i1 + 1, i2 + 1) + medal_priority(less, i1,
                                                                                                            i2)
        else:
            return medal_priority(greater, i1, i2) + country_id(matrix) + medal_priority(less, i1, i2)
    else:

        return matrix


def country_id(matrix):
    less = []
    greater = []
    if len(matrix) > 1:
        pivot = matrix[0][0]
        for i in range(len(matrix)):
            for x in matrix[i][0:1]:
                if matrix[i][0] == x:
                    if x > pivot:
                        greater.append(matrix[i])
                    else:
                        less.append(matrix[i])

        return country_id(less) + country_id(greater)

    else:

        return matrix


i1, i2 = 1, 2
countries, modalities = [int(x) for x in input().split()]
champions = []
comparison = medal_priority(get_medals_info(countries, modalities), i1, i2)
for i in range(countries):
    champions.append(str(comparison[i][0]))

print(" ".join(champions))
