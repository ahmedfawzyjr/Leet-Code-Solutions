from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
                
        return list(repeated)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(f"Example 1 Output: {sol.findRepeatedDnaSequences(s1)}") 
    # Expected: ["AAAAACCCCC", "CCCCCAAAAA"] (order may vary)
    
    # Example 2
    s2 = "AAAAAAAAAAAAA"
    print(f"Example 2 Output: {sol.findRepeatedDnaSequences(s2)}") 
    # Expected: ["AAAAAAAAAA"]
