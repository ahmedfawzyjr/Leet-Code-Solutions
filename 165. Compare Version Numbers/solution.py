class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))
        
        length = max(len(v1_parts), len(v2_parts))
        
        for i in range(length):
            v1_val = v1_parts[i] if i < len(v1_parts) else 0
            v2_val = v2_parts[i] if i < len(v2_parts) else 0
            
            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1
                
        return 0

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    v1_1, v2_1 = "1.2", "1.10"
    print(f"Input: version1 = '{v1_1}', version2 = '{v2_1}'")
    print(f"Output: {solution.compareVersion(v1_1, v2_1)}")
    # Expected: -1
    
    # Example 2
    v1_2, v2_2 = "1.01", "1.001"
    print(f"Input: version1 = '{v1_2}', version2 = '{v2_2}'")
    print(f"Output: {solution.compareVersion(v1_2, v2_2)}")
    # Expected: 0
    
    # Example 3
    v1_3, v2_3 = "1.0", "1.0.0.0"
    print(f"Input: version1 = '{v1_3}', version2 = '{v2_3}'")
    print(f"Output: {solution.compareVersion(v1_3, v2_3)}")
    # Expected: 0
