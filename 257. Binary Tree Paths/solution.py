from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Given the root of a binary tree, return all root-to-leaf paths in any order.
        A leaf is a node with no children.
        """
        if not root:
            return []
        
        paths = []
        
        def dfs(node, current_path):
            if not node:
                return
            
            # Append current node to path
            current_path += str(node.val)
            
            # If leaf node, add path to results
            if not node.left and not node.right:
                paths.append(current_path)
                return
            
            # Continue traversal
            if node.left:
                dfs(node.left, current_path + "->")
            if node.right:
                dfs(node.right, current_path + "->")
        
        dfs(root, "")
        return paths

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    #    1
    #  /   \
    # 2     3
    #  \
    #   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    
    result = sol.binaryTreePaths(root)
    print(f"Output: {result} (Expected: ['1->2->5', '1->3'])")
    
    # Test Case 2
    # 1
    root = TreeNode(1)
    result = sol.binaryTreePaths(root)
    print(f"Output: {result} (Expected: ['1'])")
