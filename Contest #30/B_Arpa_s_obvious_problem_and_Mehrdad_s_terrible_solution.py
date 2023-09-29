from collections import defaultdict

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
xor = defaultdict(int)

for num in arr:
    if num ^ x in xor:
        count += xor[num ^ x]
    
    if num in xor:
        xor[num] += 1
    
    else:
        xor[num] = 1
print(count)