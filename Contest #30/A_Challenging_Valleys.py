# t = int(input())
# for _ in range(t):
#     n = int(input())

#     arr = list(map(int, input().split()))


#     def check(l, r):
#         if l > 0:
#             if arr[l] > arr[l -1]:
#                 return False
#         if r < n - 1:
#             if arr[r] > arr[r+1]:
#                 return False
#         if arr[l] != arr[r]:
#             return False
#         return True
    
#     l, r = 0, 0

#     count = 0
#     while r < n:
#         if check(l, r):
#             r += 1
#             while r < n:
#                 if arr[r] == arr[l]:
#                     r += 1
#                 else:
#                     break
#             if r >= n: 
#                 count += 1
#             elif arr[r] > arr[r-1] and arr[l-1] > arr[l]:
#                 count += 1
#         else:
#             if l != r:
#                 l = r
#             else:
#                 r += 1
#     if count == 1:
#         print("YES")
#     else:
#         print("NO")

n = int(input())
for i in range(n):
    n = int(input())
    arr = [int(j) for j in input().split()]
    arr.append(float('inf'))
    count_valley = 0
    l,r = 0,0
    
    while r < len(arr):
        if arr[r] == arr[l]:
            r += 1
        elif arr[r] > arr[l]:
            if l-1 >= 0:
                if arr[l-1] > arr[l]:
                    count_valley += 1
                    l = r
                    r += 1
                else:
                    l = r
                    r += 1
            else:
                count_valley += 1
                l = r
                r += 1
        else:
            l = r
            r += 1
            
    if count_valley == 1:
        print("YES")
    else:
        print("NO")