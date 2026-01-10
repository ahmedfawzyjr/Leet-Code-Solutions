from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert solution.hasPathSum(root1, 22) == True, "Test case 1 failed"
    print("Test case 1 passed")
    
    # Example 2
    root2 = build_tree([1,2,3])
    assert solution.hasPathSum(root2, 5) == False, "Test case 2 failed"
    print("Test case 2 passed")
    
    # Example 3
    root3 = build_tree([])
    assert solution.hasPathSum(root3, 0) == False, "Test case 3 failed"
    print("Test case 3 passed")
    
    print("All test cases passed!")
