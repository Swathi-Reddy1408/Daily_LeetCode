class Solution:
    def maxScore(self, s: str) -> int:
        zeros_count = 0
        ans = 0
        ones_count = 0
        for i in range(len(s)):
            ones_count += 1 if s[i] == '1' else 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones_count -= 1
            else:
                zeros_count += 1
            ans = max(ans, zeros_count + ones_count)
        return ans
            

        