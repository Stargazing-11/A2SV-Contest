from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    store = defaultdict(int)
    ans = 0
    for i, num in enumerate(nums):
        num -= i
        ans += store[num]
        store[num] += 1
    
    print(ans)