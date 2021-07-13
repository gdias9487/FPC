def found_piece(n):
    miss = 0
    pieces = input().split(' ')
    complete = int((n*(n+1))/2)
    for i in pieces:
        miss += int(i)
    return (complete - miss)
n = int(input())
print(found_piece(n))