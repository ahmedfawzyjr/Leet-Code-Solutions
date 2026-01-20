from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right
            
        return -1 # Should not reach here if k is valid

if __name__ == "__main__":
    # Example 1: root = [3,1,4,null,2], k = 1
    root = TreeNode(3)
    root.left = TreeNode(1, None, TreeNode(2))
    root.right = TreeNode(4)
    
    sol = Solution()
    print(f"Kth Smallest (k=1): {sol.kthSmallest(root, 1)}") # 1
    
    # Example 2: root = [5,3,6,2,4,null,null,1], k = 3
    root2 = TreeNode(5)
    root2.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root2.right = TreeNode(6)
    
    print(f"Kth Smallest (k=3): {sol.kthSmallest(root2, 3)}") # 3
