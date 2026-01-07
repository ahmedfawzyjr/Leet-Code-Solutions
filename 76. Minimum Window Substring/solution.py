from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window approach to find minimum window substring.
        
        Time: O(m + n) where m = len(s), n = len(t)
        Space: O(n) for the character count dictionaries
        """
        if not t or not s:
            return ""
        
        # Count characters needed from t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters in t
        
        # Sliding window pointers
        left, right = 0, 0
        
        # formed is used to keep track of how many unique characters 
        # in t are present in the current window with desired frequency
        formed = 0
        
        # Dictionary to keep count of characters in current window
        window_counts = {}
        
        # Result tuple: (window length, left, right)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add character from the right to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if current character's frequency matches the desired count in t
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window until it's no longer valid
            while left <= right and formed == required:
                char = s[left]
                
                # Save the smallest window until now
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove character from the left of the window
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                # Move left pointer ahead
                left += 1
            
            # Expand the window by moving right pointer
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    print(f"Test 1: {sol.minWindow('ADOBECODEBANC', 'ABC')}")  # Expected: "BANC"
    
    # Test case 2
    print(f"Test 2: {sol.minWindow('a', 'a')}")  # Expected: "a"
    
    # Test case 3
    print(f"Test 3: {sol.minWindow('a', 'aa')}")  # Expected: ""
