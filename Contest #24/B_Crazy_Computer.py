n, c = map(int, input().split())
times = list(map(int, input().split()))

last = 0
count = 0

for time in times:
    if time - last <= c:
        count += 1
    else:
        count = 1
    
    last = time

print(count)