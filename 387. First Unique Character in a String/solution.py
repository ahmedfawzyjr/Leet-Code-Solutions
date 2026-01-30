from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode")) # Expected: 0
    print(sol.firstUniqChar("loveleetcode")) # Expected: 2
    print(sol.firstUniqChar("aabb")) # Expected: -1
