n = int(input())
stones = [int(i) for i in input().split()]
scraps = 0
steps = 0
stones_area = 0

for i in stones:
    stones_area += i

stones_in_stair = (n * (n - 1)) // 2
base = stones_area - stones_in_stair

if base % n == 0 and base > 0:
    hBase = base // n

    for i in range(n):
        scraps += stones[i] - (hBase + i)
        if stones[i] > (hBase + i):  # Compara a escada perfeita com as pilhas de pedras e move as pedras que sobram
            steps += stones[i] - (hBase + i)
    if scraps == 0:
        print(steps)
    else:
        print(-1)

else:
    print(-1)
