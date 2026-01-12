from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
                    
        backtrack(0, [])
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "aab"
    expected1 = [["a","a","b"],["aa","b"]]
    result1 = solution.partition(s1)
    # Sort inner lists and outer list for comparison as order doesn't strictly matter for correctness but usually follows DFS order
    # However, for exact match with LeetCode output format which is usually ordered:
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed: {result1}"
    print("Test case 1 passed")
    
    # Example 2
    s2 = "a"
    expected2 = [["a"]]
    result2 = solution.partition(s2)
    assert result2 == expected2, f"Test case 2 failed: {result2}"
    print("Test case 2 passed")
