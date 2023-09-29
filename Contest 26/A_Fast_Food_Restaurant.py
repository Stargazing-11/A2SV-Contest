def maximum_visitors(a, b, c):
    min_portions = min(a, b, c)
    max_portions = max(a, b, c)
    
    return min_portions + max(max_portions - 1, 0)

# Input: Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    a, b, c = map(int, input().split())
    result = maximum_visitors(a, b, c)
    print(result)
