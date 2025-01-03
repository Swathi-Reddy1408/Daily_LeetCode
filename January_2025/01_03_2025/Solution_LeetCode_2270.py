class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum_half = sum(nums) / 2
        left = 0
        ans = 0
        for i in range(len(nums)-1):
            left += nums[i]
            if left >= total_sum_half:
                ans += 1
        return ans