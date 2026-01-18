class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        map_s_t = {}
        map_t_s = {}
        
        for char_s, char_t in zip(s, t):
            if (char_s in map_s_t and map_s_t[char_s] != char_t) or \
               (char_t in map_t_s and map_t_s[char_t] != char_s):
                return False
                
            map_s_t[char_s] = char_t
            map_t_s[char_t] = char_s
            
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    s = "egg"
    t = "add"
    print(f"Example 1: {sol.isIsomorphic(s, t)}") # Expected: True
    
    # Example 2
    s = "foo"
    t = "bar"
    print(f"Example 2: {sol.isIsomorphic(s, t)}") # Expected: False
    
    # Example 3
    s = "paper"
    t = "title"
    print(f"Example 3: {sol.isIsomorphic(s, t)}") # Expected: True
