
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

My mind immediately thought of using a priority queue because if I know each subarray sum and keep on tracking which 3 subarrays will give me the maximum sum, then I can just return those indices but it adds so much complexity to the problem.

### Challenges with This Approach
**Tracking Lexicographically Smaller Subarrays** 

The question also states that if we have multiple subarrays satisfying the conditions (e.g., if some subarrays' sums are the same), we need to return the lexicographically smaller indexed subarray.

**Example:**  
For the above question, there could be another solution possible which is indices `[1, 3, 5]` that still gives the same total sum `23`.  
However, `[0, 3, 5]` is the lexicographically smallest solution.


### Backtracking Solution

A good solution would be to use backtracking. At each index with a subarray of length `k` generated in the array, we have two choices:
1. **Include the subarray sum in the total sum.**
2. **Skip the subarray and go for the next subarray sum.**
This approach gives the output but involves a time complexity of `O(2^n)` because at each point, we are taking two decisions and sometimes solving the same subproblem multiple times.

### Optimizing with Caching
To optimize, we can use caching. Once we determine the decision at each point, we store it in a cache. This way, we avoid running the algorithm for choices we have already solved.

## Memoization (Top-Down Approach)

It involves three steps:

1. **Find the Subarray Sum at Every Index**  
   Think of what the subarray sum at that index would be if you include that index in your answer. This can be done with a two-pointer approach.

2. **Make the Choice at Each Index**  
   At each index, decide if including it could result in the maximum sum for the 3 chosen subarrays.

3. **Repeat for All Indices**  
   Repeat the above step for every index. Append whichever indices result in the maximum sum to the result.

### Choices at Each Step
For each index `i`:
- **Including `i`**  
  `nums[i] + find_max_sum(i + k, count_of_subarrays + 1)`
- **Skipping `i`**  
  `find_max_sum(i, count_of_subarrays)`
The base case occurs when i exceeds the bounds of the array and cannot form a valid subarray or count_of_subarrays exceeds 3.
In these scenarios, the function should return 0.

### Caching Results
To cache the results, maintain a dynamic programming (DP) hashmap with `(i, count_of_subarrays)` as the tuple key and the sum as the value. 

When the algorithm starts at the `0th` index:
- The results are cached.  
- The next time it is called, the results will be returned directly from the DP cache.

## Time Complexity

- **Optimized Time Complexity**: `O(n)`  
  All the choices are executed only once, resulting in linear time complexity compared to the exponential `O(2^n)` time complexity of backtracking.

