def Fix_Balance(n, r):
    limit = n - r
    balance = [int(i) for i in input()]
    i, j = 0, 1
    while len(balance) > limit:
        if j <= len(balance) - 1:
            if balance[j] > balance[i]:  # Verifica se o próximo é maior que o atual.
                del balance[i]
                i, j = 0, 1
            else:
                i, j = i + 1, j + 1  # Se não for, pula os mais um nos indices e compara os dois próximos.
        else:
            del balance[i]
            i -= 1
    return "".join(map(str, balance))


while True:
    a = input()
    if a:
        n, r = [int(i) for i in a.split(" ")]
        print(Fix_Balance(n, r))
    else:
        break
