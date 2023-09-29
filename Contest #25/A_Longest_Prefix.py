from collections import Counter
t  = int(input())

for _ in range(t):
    a, b = input().split()

    counted_b = Counter(b)

    count = 0

    for leter in a:
        if counted_b[leter] > 0:
            counted_b[leter] -= 1
            count += 1
        else:
            break
    print(count)