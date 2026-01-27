class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Each non-null node provides 2 slots and consumes 1 slot.
        # Each null node consumes 1 slot.
        # We start with 1 slot (for the root).
        slots = 1
        
        for node in preorder.split(','):
            # Consume one slot for the current node
            slots -= 1
            
            # If slots < 0, it's invalid (more nodes than slots available)
            if slots < 0:
                return False
            
            # If it's not a null node, it adds two more slots
            if node != '#':
                slots += 2
        
        # In the end, all slots should be consumed
        return slots == 0

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    preorder1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print(f"Example 1: {sol.isValidSerialization(preorder1)}") # Expected: True
    
    # Example 2
    preorder2 = "1,#"
    print(f"Example 2: {sol.isValidSerialization(preorder2)}") # Expected: False
    
    # Example 3
    preorder3 = "9,#,#,1"
    print(f"Example 3: {sol.isValidSerialization(preorder3)}") # Expected: False
