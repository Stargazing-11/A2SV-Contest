q = int(input())
requests = []

for i in range(q):
    old, new = input().split()
    requests.append((old, new))
    store = {}

for old, new in requests:
    if old in store:
        cur = store[old]
        store[new] = cur
        del store[old]
    else:
        store[new] = old

print(len(store))

for old, new in store.items():
    print(new, old)