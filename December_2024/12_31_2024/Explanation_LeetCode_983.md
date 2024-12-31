# Leetcode 983 - Minimum Cost For Tickets

(All rights are reserved to LeetCode Inc.)

## Solution Credit

I came up with the solution by myself😊 and today marks the day that I have completed my Leetcode Decemeber Coding Challenge and I have attached my badge here!

## Problem Description

We have been given 2 inputs:
``` python
days = [1,4,6,7,8,20], costs = [2,7,15]
```

The question says we have some travel plans in next year on the days given as days input array. There are three types of passes available: costs[0] for a 1-day pass, costs[1] for a 7-day pass, and costs[2] for a 30-day pass. The goal is to travel on the given days while minimizing the total cost, which requires careful selection of the passes. The maximum size of the days array is 365, and costs always contains three elements.
```
Example Output:
```python
output = 11
```
Explanation:

On Day 1, I purchase a 1-day pass (valid until Day 2) costing costs[0] = 2.
On Day 4, I purchase a 7-day pass (valid until Day 11) costing costs[1] = 7.
On Day 20, I purchase another 1-day pass costing costs[0] = 2.
The total cost is 11.

## My Intuition

As soon as I saw the problem, I quickly figured out it's a dp problem. Because if something needs to be minimized or maximized the best approach would be to use DP. The idea is to maintain a variable, curDay, to track which pass would be most efficient for the current day. We start at day 0 and continue until the last day in the array.

Approach:


At each step, we check if the curDay is the day we are travelling. 

If we are travelling then we need to buy the pass and that's when we will have 3 choices whether to purchase 1 day pass or 7 day pass or 30 day pass. This takes us to the recursion path of again 3 choices every time with cost being added of that pass. Remember we need to minimize the cost so whatever decision we choose we need to return minimum among them. So we would be using min function to take care of it.

If we are not travelling we still need to run the algorithm but by just incrementing the day.

Checking conditions at Each Step and branching out into three possibilities:

If it is a travel day:
We buy a pass, and we have three choices: a 1-day pass, a 7-day pass, or a 30-day pass. Each choice creates a recursive call to calculate the cost from that point forward, with the respective cost of the pass added. 

```python
res = min(cost[0] + func(curDay + 1) ,  cost[1] + func(curDay + 7), cost[2] + func(curDay + 30) )
```
If it is not a travel day:
We simply move to the next day without buying a pass.

```python
res = func(curDay + 1)
```
Base Case:

The calculation only needs to be performed up to the last travel day. Once curDay exceeds the last travel day, the algorithm should stop since there is no point in calculating above and beyond. This is our basecase.

## Optimization with Memoization:

For each travel day, there are three choices to explore, leading to exponential time complexity in the recursive solution. Specifically, the complexity is $O(3^k)$, where k represents the number of days we actually consider (some days might be skipped due to the validity periods of the 7-day or 30-day passes). To improve efficiency, we store the results of computed choices. If the algorithm revisits the same day, it retrieves the precomputed result, avoiding redundant calculations. This technique, known as DP-Memoization or the Top-Down Approach, reduces the time complexity to $O(k)$. The algorithm now processes each day only once, reusing stored results for subsequent decisions.


## Time Complexity

Without optimization: $O(3^k)$ due to three recursive branches at each step.
With memoization: $O(k)$, as each day's cost is calculated once and reused.