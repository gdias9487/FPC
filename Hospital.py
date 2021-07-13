def check_priority_by_plan(people, n):
    premium = []
    diamond = []
    gold = []
    silver = []
    bronze = []
    rest = []
    for line in range(n):

        if people[line][1] == 'premium':
            premium.append(people[line])

        elif people[line][1] == 'diamante':
            diamond.append(people[line])

        elif people[line][1] == 'ouro':
            gold.append(people[line])

        elif people[line][1] == 'prata':
            silver.append(people[line])

        elif people[line][1] == 'bronze':
            bronze.append(people[line])

        else:
            rest.append(people[line])

    if len(check_priority_by_number(premium)) > 0:
        for i in range(len(check_priority_by_number(premium))):
            print(check_priority_by_number(premium)[i][0])

    if len(check_priority_by_number(diamond)) > 0:
        for i in range(len(check_priority_by_number(diamond))):
            print(check_priority_by_number(diamond)[i][0])

    if len(check_priority_by_number(gold)) > 0:
        for i in range(len(check_priority_by_number(gold))):
            print(check_priority_by_number(gold)[i][0])

    if len(check_priority_by_number(silver)) > 0:
        for i in range(len(check_priority_by_number(silver))):
            print(check_priority_by_number(silver)[i][0])

    if len(check_priority_by_number(bronze)) > 0:
        for i in range(len(check_priority_by_number(bronze))):
            print(check_priority_by_number(bronze)[i][0])

    if len(check_priority_by_number(rest)) > 0:
        for i in range(len(check_priority_by_number(rest))):
            print(check_priority_by_number(rest)[i][0])


def check_priority_by_number(matrix):
    less = []
    equal = []
    greater = []

    if len(matrix) > 1:
        pivot = matrix[0][2]
        for i in range(len(matrix)):
            for x in matrix[i]:
                if matrix[i][2] == x:
                    if x > pivot:
                        greater.append(matrix[i])
                    elif x < pivot:
                        less.append(matrix[i])
                    else:
                        equal.append(matrix[i])

        return check_priority_by_number(greater) + alphabetical_order(equal) + check_priority_by_number(less)

    else:

        return matrix


def alphabetical_order(matrix):
    less = []
    equal = []
    greater = []

    if len(matrix) > 1:
        pivot = matrix[0][0]
        for i in range(len(matrix)):
            for j in matrix[i]:
                if matrix[i][0] == j:
                    if j < pivot:
                        less.append(matrix[i])
                    elif j > pivot:
                        greater.append(matrix[i])
                    else:
                        equal.append(matrix[i])

        return alphabetical_order(less) + equal + alphabetical_order(greater)

    else:

        return matrix


people = []
n = int(input())
for i in range(n):
    patients = [x for x in input().split()]
    patients = patients[0], patients[1], int(patients[2])
    people.append(patients)
check_priority_by_plan(people, n)
