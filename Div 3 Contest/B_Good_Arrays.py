t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    c = arr.count(1)

    if sum(arr) < c + n or n == 1:
        print("NO")
    else:
        print("YES")