# Leetcode 1422 - Maximum Score After Splitting a String

(All rights are reserved to LeetCode Inc.)

## Solution Credit

This solution is entirely my own 😊.

## Problem Description

We have been given a input string:
``` python
s = "011101"
```

The task is to determine the maximum score obtained by splitting the string at any index. The score is calculated as the sum of the count of 0s on the left side and the count of 1s on the right side of the split. The goal is to find the maximum possible score across all splits.

Example Output:
```python
output = 5
```
Explanation:

Splitting the string at index 0: "0" and "11101".
Left side: 1 occurrence of 0.
Right side: 4 occurrences of 1.
Total score: 1 + 4 = 5

Splitting the string at index 1: "01" and "1101".
Left side: 1 occurrence of 0.
Right side: 3 occurrences of 1.
Total score: 1+3=4.

Splitting the string at index 2: "011" and "101".
Left side: 1 occurrence of 0.
Right side: 2 occurrences of 1.
Total score: 1+2=3.
Continuing this process, we observe that the maximum score of 5 is achieved when the string is split at index 0.


## My Intuition

If we know the total count of 1s in the string, we can compute the score for each split efficiently. The idea is simple:

Traverse the string while maintaining a count of 0s (for the left side) and dynamically updating the count of 1s (for the right side).
For each index, calculate the score as the sum of the counts of 0s on the left and 1s on the right.

Approach:
1. Precompute the total number of 1s:

Traverse the string and count all the 1s to initialize a variable ones_count.

```python
for i in range(len(s)):
    ones_count += 1 if s[i] == '1' else 0
```
2. Calculate the maximum score:

Traverse the string again, updating the count of 0s and adjusting the count of 1s as we move along.
At each index, compute the score as zeros_count + ones_count and update the maximum score.

```python
for i in range(len(s) - 1):
    if s[i] == '1':
        ones_count -= 1
    else:
        zeros_count += 1
    ans = max(ans, zeros_count + ones_count)
```

## Time Complexity

This algorithm runs in O(n) time. The first traversal is used to precompute the count of 1s, and the second traversal calculates the maximum score. This results in a total complexity of O(n+n) = O(n).