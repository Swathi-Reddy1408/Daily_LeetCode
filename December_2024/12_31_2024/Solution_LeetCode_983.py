class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1] * (days[-1] + 1)
        def dfs(curDay):
            if curDay > days[-1]:
                return 0
            if dp[curDay] != -1:
                return dp[curDay]
            if curDay in days:
                dp[curDay] = min(costs[0] + dfs(curDay + 1), costs[1] + dfs(curDay + 7), costs[2] + dfs(curDay + 30))
            else:
                dp[curDay] = dfs(curDay + 1)
            return dp[curDay]
        print(dfs(0))
        return dfs(0)

        