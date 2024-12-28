class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        #Create sub-array sums at each index.
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] + nums[i] - nums[i-k])
        dp = {}

        #Using subarray sums, we find the max_sum by including the index or skipping the index.
        #Use dp memoization to cache the results for every choice.
        def get_max_sum(i, count):
            if count == 3 or i > len(nums) - k:
                return 0
            if (i,count) in dp:
                return dp[(i, count)]
            include = k_sums[i] + get_max_sum(i+k, count+1)
            skip = get_max_sum(i+1, count)
            dp[(i, count)] = max(include, skip)
            return dp[(i, count)]
        
        #Run the algorithm for every index. Not technically every index since results are cached!
        def get_indices():
            i = 0
            indices = []
            while i <= len(nums) - k and len(indices) < 3:
                include = k_sums[i] + get_max_sum(i+k, len(indices) + 1)
                skip = get_max_sum(i+1, len(indices))
                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1
            return indices
        return get_indices() 


        