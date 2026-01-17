from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                # If it's the last node in the current level, add to result
                if i == level_length - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    #    1
    #  /   \
    # 2     3
    #  \     \
    #   5     4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(f"Example 1: {sol.rightSideView(root1)}") # Expected: [1, 3, 4]

    # Example 2
    # 1
    #  \
    #   3
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(f"Example 2: {sol.rightSideView(root2)}") # Expected: [1, 3]

    # Example 3
    root3 = None
    print(f"Example 3: {sol.rightSideView(root3)}") # Expected: []
