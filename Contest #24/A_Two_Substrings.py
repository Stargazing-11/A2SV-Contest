s = input()

i = 0 
found = "NO"
while i < len(s) - 1:
    if s[i:i+2] == "AB" and "BA" in s[i+2:]:
        found = "YES"
        break
    
    elif s[i:i+2] == "BA" and "AB" in s[i+2:]:
        found = "YES"
        break
    else:
        i += 1
        
print(found)