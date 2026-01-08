from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Given a string s containing only digits, return all possible valid IP addresses
        that can be formed by inserting dots into s.
        
        A valid IP address consists of exactly four integers separated by single dots.
        Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
        
        Approach: Backtracking
        - Try all possible ways to split the string into 4 parts
        - Each part must be a valid segment (0-255, no leading zeros)
        - Time: O(3^4) = O(81) since each segment can be 1-3 digits
        """
        result = []
        
        def is_valid(segment: str) -> bool:
            # Check for valid segment: 0-255, no leading zeros (except "0" itself)
            if len(segment) > 3 or len(segment) == 0:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return int(segment) <= 255
        
        def backtrack(start: int, parts: List[str]) -> None:
            # If we have 4 parts and used all characters, we found a valid IP
            if len(parts) == 4:
                if start == len(s):
                    result.append('.'.join(parts))
                return
            
            # Try segments of length 1, 2, and 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, parts + [segment])
        
        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "25525511135"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {sol.restoreIpAddresses(s1)}")
    # Expected: ["255.255.11.135","255.255.111.35"]
    
    # Example 2
    s2 = "0000"
    print(f"\nInput: s = \"{s2}\"")
    print(f"Output: {sol.restoreIpAddresses(s2)}")
    # Expected: ["0.0.0.0"]
    
    # Example 3
    s3 = "101023"
    print(f"\nInput: s = \"{s3}\"")
    print(f"Output: {sol.restoreIpAddresses(s3)}")
    # Expected: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
