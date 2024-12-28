
# Leetcode 689 - Maximum Sum of 3 Non-Overlapping Subarrays

(All rights are reserved to LeetCode Inc.)

## Solution Credit

I learned the solution from Neetcode's channel on YouTube.  
Thanks, Neetcode! 😊

## Problem Description

The problem says given an array and `k` like below:
```python
nums = [1,2,1,2,6,7,5,1]
k = 2
```

We need to find starting indices of 3 subarrays of length `k` such that the chosen subarrays' sum is the maximum of all.

## Explanation

At least that's what I understood when I looked at the question.

### Output
The output is:
```python
[0, 3, 5]
```

### Reasoning
- At index `0`, the subarray with the given length is `[1, 2]` and its sum is `3`.
- At index `3`, the subarray with the given length is `[2, 6]` and its sum is `8`.
- At index `5`, the subarray with the given length is `[7, 5]` and its sum is `12`.

The total sum is `3 + 8 + 12 = 23`, which is the maximum sum we get among all subarrays of length `2`.

## Initial Thought Process

My mind immediately thought of using a priority queue because if I know each subarray sum and keep on tracking which 3 subarrays will give me the maximum sum, then I can just return those indices.

### Challenges with This Approach
1. **Tracking Lexicographically Smaller Subarrays**  
   The question also states that if we have multiple subarrays satisfying the conditions (e.g., if some subarrays' sums are the same), we need to return the lexicographically smaller indexed subarray.

   **Example:**  
   For the above question, there could be another solution possible which is indices `[1, 3, 5]` that still gives the same total sum `23`.  
   However, `[0, 3, 5]` is the lexicographically smallest solution.

2. **Managing Priority Queue Size**  
   If we know the sum, how do we keep track of those indices without exceeding 3, since we only need to find 3 indices of subarrays that resulted in the maximum sum?

