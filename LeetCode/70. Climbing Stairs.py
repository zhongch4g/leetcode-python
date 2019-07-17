#-*-coding:utf-8 -*-
"""
    70. Climbing Stairs
    Directed by user zhongch4g
    current system date 2017/5/2
"""
class Solution(object):
    def climbStairs(self, n):
        return self.helper(n, {})

    def helper(self, n, memo):
        if n in memo:
            print(n)
            return memo[n]

        if n == 1 or n == 0:
            return 1
        if n == 2:
            return 2
        one = self.helper(n-1, memo)

        two = self.helper(n-2, memo)
        memo[n] = one + two
        return one + two


    # dynamic programming
    def climbStairs2(self, n):
        if n == 1 or n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]


instance = Solution()
print (instance.climbStairs2(35))