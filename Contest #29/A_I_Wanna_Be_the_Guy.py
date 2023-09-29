n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

all = set(second[1:] + first[1:])
if len(all) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

