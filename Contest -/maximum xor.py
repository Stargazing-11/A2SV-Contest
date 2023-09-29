t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    ans = 0

    for i in range(len(arr)):
        for j in range(i + 1, n):
            ans = max(ans, arr[i] ^ arr[j])
    print(ans)