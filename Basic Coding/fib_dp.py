# Dynamic Programming Approach
def fib_dp(n):
    if n <= 1:
        return [0] if n == 0 else [0, 1]
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp
n = int(input("Enter n: "))
print(fib_dp(n))        

class Solution(object):
    def fib_all(self, n):
        if n <= 0:
            return []

        result = []
        a, b = 0, 1

        for _ in range(n):
            result.append(a)
            a, b = b, a + b

        return result