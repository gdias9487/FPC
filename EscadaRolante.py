def escalator(l):
    totaltime = 10
    for i in range(1, n):
        print(i)
        totaltime += min(10, l[i] - l[i-1])
    return totaltime
l = []
n = int(input())
for i in range(n):
    l.append(int(input()))
print(escalator(l))