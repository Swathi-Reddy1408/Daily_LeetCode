class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [-1] * (high + 1)
        mod = 10**9 + 7
        def dfs(res):
            count = 0
            if res > high:
                return 0
            if dp[res] != -1:
                return dp[res]
            if res >= low and res <= high:
                count = dfs(res+zero) + dfs(res+one) + 1
            else:
                count = dfs(res+zero) + dfs(res+one)            
            dp[res] = count % mod
            return dp[res]
        
        return dfs(0)
            
            
            
            
