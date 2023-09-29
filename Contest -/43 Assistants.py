t = int(input())

for _ in range(t):
    n = int(input())
    max_v = float('-inf')
    slots = []
    for i in range(n):
        a, b = map(int, input().split())
        max_v = max(max_v, a, b)

        slots.append((a, b))

    slote_range = [0 for i in range(max_v+1)]

    for a, b in slots:
        slote_range[a] += 1
        slote_range[b] -= 1
    
    for i in range(len(slote_range)):
        add = slote_range[i-1] if i > 0 else 0
        slote_range[i] += add

    print(max(slote_range))