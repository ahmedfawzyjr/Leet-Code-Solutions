"""
LeetCode 3699: Number of ZigZag Arrays I

A ZigZag array of length n must satisfy:
1. Each element lies in the range [l, r]
2. No two adjacent elements are equal
3. No three consecutive elements form a strictly increasing or strictly decreasing sequence

This means the array must alternate between increasing and decreasing trends - a true "zigzag" pattern.

Example 1: n=3, l=4, r=5
Valid arrays: [4,5,4], [5,4,5] -> Output: 2

Example 2: n=3, l=1, r=3
Valid arrays: [1,2,1], [1,3,1], [1,3,2], [2,1,2], [2,1,3], [2,3,1], [2,3,2], [3,1,2], [3,1,3], [3,2,3] -> Output: 10

Approach:
- Use dynamic programming with state: (last_value, last_trend)
  - last_value: value at the previous position
  - last_trend: 0 = increasing (prev_prev < prev), 1 = decreasing (prev_prev > prev)
- For each new position, we can only add values that:
  1. Are different from the previous value
  2. Have a different trend than the last trend (to maintain zigzag)

Time Complexity: O(n * (r-l) * (r-l)) = O(n * range^2)
Space Complexity: O(range^2) for the DP table
"""

def numberOfZigzagArrays(n: int, l: int, r: int) -> int:
    MOD = 10**9 + 7
    
    # Special case for n < 3: no constraints beyond adjacency
    if n < 3:
        # For n=2: choose any 2 different values from [l, r]
        # Since constraints start at n=3, we handle separately
        # But based on problem constraints, n >= 3
        pass
    
    # Initialize DP for positions 1 and 2
    # curr[(last_val, last_trend)] = count of ways to reach current position
    # trend: 0 = increasing, 1 = decreasing
    curr_dp = {}
    
    # Build initial state after placing first 2 elements
    range_count = r - l + 1
    
    # For position 2: choose any 2 different values
    for val1 in range(l, r + 1):
        for val2 in range(l, r + 1):
            if val1 != val2:
                # Determine trend from val1 to val2
                trend = 0 if val2 > val1 else 1  # 0=increasing, 1=decreasing
                key = (val2, trend)
                curr_dp[key] = curr_dp.get(key, 0) + 1
    
    # Fill DP for positions 3 to n
    for pos in range(3, n + 1):
        next_dp = {}
        
        for (prev_val, last_trend), count in curr_dp.items():
            # Try placing each value at current position
            for new_val in range(l, r + 1):
                # Constraint 1: Adjacent elements must be different
                if new_val == prev_val:
                    continue
                
                # Determine trend from prev_val to new_val
                new_trend = 0 if new_val > prev_val else 1  # 0=increasing, 1=decreasing
                
                # Constraint 2: Trends must alternate (zigzag)
                if new_trend == last_trend:
                    continue
                
                # Add to next state
                key = (new_val, new_trend)
                next_dp[key] = (next_dp.get(key, 0) + count) % MOD
        
        curr_dp = next_dp
    
    # Sum all valid sequences of length n
    return sum(curr_dp.values()) % MOD


# Test cases
if __name__ == "__main__":
    # Example 1
    result1 = numberOfZigzagArrays(3, 4, 5)
    print(f"Example 1: numberOfZigzagArrays(3, 4, 5) = {result1}")
    assert result1 == 2, f"Expected 2, got {result1}"
    
    # Example 2
    result2 = numberOfZigzagArrays(3, 1, 3)
    print(f"Example 2: numberOfZigzagArrays(3, 1, 3) = {result2}")
    assert result2 == 10, f"Expected 10, got {result2}"
    
    print("All test cases passed!")
