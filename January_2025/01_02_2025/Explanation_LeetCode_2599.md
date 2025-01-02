# Leetcode 2599 - Count Vowel Strings in Ranges

(All rights are reserved to LeetCode Inc.)

## Solution Credit

I came up with the solution by myself as I solved couple of problems before using prefix_sum concept.

## Problem Description

We have been given 2 inputs:
``` python
words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
```

The task is to determine how many "good" words exist within the specified ranges for each query. While the term "good word" is not directly mentioned in the problem, I defined it for clarity. A "good word" is any word that starts and ends with a vowel (the vowels don’t have to be the same). The goal is to return the count of such words for the inclusive range specified by each query.

```
Example Output:
```python
output = [2,3,0]
```
Explanation:

For the first query [0, 2], there are two "good" words: ['aba', 'ece'].
For the second query [1, 4], there are three "good" words: ['ece', 'aa', 'e']. The word 'bcb' is excluded since it is not a "good" word.
For the third query [1, 1], there are no "good" words, so the count is 0.

## My Intuition

I understood this as a prefix sum problem because Prefix sum is particularly useful when the task involves calculating cumulative totals, where the sum at the (i+1)th index depends on the sum at the ith index.

Approach:

To leverage prefix sum, some precomputation is needed.

The precomputation involves determining how many "good" words exist up to each index. So for each query with a specified start and end range, if we know the total number of "good" words up to the end index, we can simply subtract the total up to the (start-1) index to get the count of "good" words within that range.

Identifying a "Good" Word
To check if a word is "good," we maintain a set of vowels. For each word, we check if both the first and last characters are present in the set. The use of a set ensures that this check operates with a time complexity of O(1).

```python
for i in range(0, len(words)):
    if isGoodWord(words[i]):
        sum += 1
    prefix_sum[i] = sum
```
Once we have this pre-computation ready all we have to do is, answer each query.

```python
for [start, end] in queries:
    if start == 0: #if start = 0 then the number of good words is just cumulative sum till that index.
        ans.append(prefix_sum[end])
    else:
        ans.append(prefix_sum[end] - prefix_sum[start-1])
```

## Time Complexity

The time complexity of this algorithm is O(n), as it involves precomputing the prefix sum by checking every word in the words array and answering each query sequentially. This results in O(n+n)=O(n).