t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    memo = {}

    def dp(n, m, turn):
        if n == 0 and m == 0 and turn == 0:
            return True
        if n == 0 and m == 0 and turn == 1:
            return False
        
        if (n, m, turn) in memo:
            return memo[(n, m, turn)]

        ans = False
        if n > 0 and m > 0:
            ans |= dp(n-1, m-1, 1 - turn)
        if n > 0:
            ans |= dp(n-1, m, 1 - turn)
        if m > 0:
            ans |= dp(n, m-1, 1 - turn)

        memo[(n, m, turn)] = ans
        return memo[(n, m, turn)]

    ans = dp(n, m, 1)

    if ans:
        print("hasan")
    else:
        print("abdullah")


# def solve_game(n, m):
#     dp = [[False for _ in range(2)] for _ in range(2)]
#     dp[n % 2][m % 2] = True

#     for i in range(n, -1, -1):
#         for j in range(m, -1, -1):
#             if i < n or j < m:
#                 dp[i % 2][j % 2] = False
#                 if i + 1 <= n and j + 1 <= m:
#                     dp[i % 2][j % 2] |= dp[(i + 1) % 2][(j + 1) % 2]
#                 if i + 1 <= n:
#                     dp[i % 2][j % 2] |= dp[(i + 1) % 2][j % 2]
#                 if j + 1 <= m:
#                     dp[i % 2][j % 2] |= dp[i % 2][(j + 1) % 2]

#     return dp[0][0]

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     winner = "hasan" if solve_game(n, m) else "abdullah"
#     print(winner)
