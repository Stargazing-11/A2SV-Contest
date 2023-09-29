t = int(input())

for _ in range(t):
    string = input()
    ans = set()
    
    left = 0
    while left < len(string):
        right = left + 1
        c = 1
        while right < len(string) and string[right] == string[right-1]:
            right += 1
            c += 1
        if c % 2 == 1:
            ans.add(string[left])
        
        left += c
    ans = list(ans)
    print("".join(sorted(ans)))