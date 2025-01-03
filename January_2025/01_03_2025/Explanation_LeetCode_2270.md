# Leetcode 2270 - Number Of Ways To Split Array

(All rights are reserved to LeetCode Inc.)

## Solution Credit

I came up with the solution by myself.

## Problem Description

We have been given an input array nums:
``` python
nums = [10,4,-8,7]
```

Given an input array nums, the task is to determine the number of valid indices i where we can split the array such that:
Sum of elements on the left side ≥ Sum of elements on the right side.

```
Example Output:
```python
output = 2
```
Explanation:

Split at index 0: Left: [10], Right: [4, -8, 7]
10≥4−8+7 → True

Split at index 1: Left: [10, 4], Right: [-8, 7]
10+4≥−8+7 → True

Split at index 2: Left: [10, 4, -8], Right: [7]
10+4−8≥7 → False

Split at index 3: Not possible, as there’s no right portion.

So, the total number of valid splits is 2.


## My Intuition

When solving this, I started by thinking about how to efficiently calculate both the left and right sums for every possible split index. Initially, I thought of precomputing the prefix sum (left_sum) and suffix sum (right_sum) for the entire array, but that approach felt unnecessarily cumbersome, requiring multiple loops.

Then, it hit me why not compute everything in one pass?

Here’s the breakthrough idea:

The sum of the right portion can be expressed as:

right_sum = total_sum − left_sum
So, the condition:
left_sum ≥ right_sum
can be rewritten as:
left_sum ≥ total_sum − left_sum
Simplify further:
2 * left_sum ≥ total_sum
or equivalently:
left_sum ≥ total_sum / 2
​
 This equation eliminates the need for extra variables and precomputations! We can directly compute the left sum in a single loop and check the condition for each split.

```python
total_sum_half = sum(nums) / 2
left = 0
ans = 0
for i in range(len(nums)-1):
    left += nums[i]
    if left >= total_sum_half:
        ans += 1
return ans
```

## Time Complexity

The time complexity of this algorithm is O(n).