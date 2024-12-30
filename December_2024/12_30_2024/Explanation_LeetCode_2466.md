# Leetcode 2466 - Count Ways To Build Good Strings

(All rights are reserved to LeetCode Inc.)

## Solution Credit

I came up with the solution by myself. Atleast the memoization technique. 😊

## Problem Description

We have been given 4 inputs:
``` python
low = 3, high = 3, zero = 1, one = 1
```

The question says we need to count the number of good strings. Good strings are formed by appending 0s or 1s, and we can append both. We are restricted to a given number of zeroes and ones (zero and one). This means:

I can form strings by appending zeroes up to zero times and ones up to one times.

Repeating this process, all strings with lengths between low and high (inclusive) are considered good strings.

Example Input:
```python
low = 3
high = 3
zero = 1
one = 1
```
Example Output:
```python
output = 8
```
Explanation:

The strings that can be formed while staying within the low and high limit are:

"000", "001", "010", "011", "100", "101", "110", "111".
Return the ans % 10^9 + 7

## My Intuition

Looking at the problem, I understood that I don't literally have to create the strings. Instead, I can focus on the lengths I can expect by appending zeroes or ones.

Approach:


At each step, check if we can use zero or one to increment the expected length.

If the new length is within low and high, increment the count.

If the length is outside this range, only increment zeroes and ones without adding to the count.

Two Choices at Each Step:

If the length is valid:
```python
count = dfs(reslen + zeroes) + dfs(reslen + ones) + 1
```
If the length is invalid:
```python
count = dfs(reslen + zeroes) + dfs(reslen + ones)
```
Base Case:

If the length exceeds high, return 0.

## Optimization with Memoization:

Use a dp array to cache results for already-computed lengths. This avoids redundant calculations and improves efficiency.

Modulo Operation:

remember we need to return the final answer modulo $10^9 + 7$ as it is asked in the question.

## Time Complexity

Without optimization (pure recursion), the time complexity would be $O(2^n)$ since there are two choices at each step. With memoization, results are computed only once and reused, reducing the time complexity to $O(n)$, where n is the maximum length (high).

