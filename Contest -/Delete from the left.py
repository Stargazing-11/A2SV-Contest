s = input()
t = input()

l, r = len(s) -1, len(t) -1 

count = 0
while l >= 0 and r >= 0:
    if s[l] != t[r]:
        break
    else:
        count += 1
    l -= 1
    r -= 1
print((len(s) - count) + (len(t) - count))