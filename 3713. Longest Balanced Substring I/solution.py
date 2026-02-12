class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Iterate over all possible start points
        for i in range(n):
            counts = {}
            # Iterate over all possible end points
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                
                # Check if the substring s[i:j+1] is balanced
                # A substring is balanced if all distinct characters appear the same number of times.
                
                # Get the set of frequencies of characters present in the substring
                distinct_freqs = set(counts.values())
                
                # If there's only one distinct frequency, it means all characters appear the same number of times
                if len(distinct_freqs) == 1:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases from the problem description
    test_cases = [
        ("abbac", 4),
        ("zzabccy", 4),
        ("aba", 2),
    ]
    
    for s, expected in test_cases:
        result = sol.longestBalanced(s)
        print(f"Input: s = \"{s}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print("-" * 20)
