# 1833. Maximum Ice Cream Bars

## Approach
- Use a counting-sort style frequency array because all prices are bounded by `10^5`.
- Traverse prices from smallest to largest and buy as many bars as possible while staying within `coins`.

## Why this works
- Buying cheaper bars first always leaves the most budget for additional purchases.
- Since the prices are sorted by cost, the greedy process reaches the maximum count.

## Complexity
- Time: `O(n + max(costs))`
- Space: `O(max(costs))`
