# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two given nodes in a binary tree.
        
        Args:
            root: The root of the binary tree.
            p: The first node.
            q: The second node.
            
        Returns:
            The lowest common ancestor node.
        """
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right

if __name__ == "__main__":
    # Test Case 1
    #       3
    #      / \
    #     5   1
    #    / \ / \
    #   6  2 0  8
    #     / \
    #    7   4
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    
    sol = Solution()
    
    # LCA of 5 and 1 should be 3
    p = root.left
    q = root.right
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val}: {lca.val} (Expected: 3)")
    
    # LCA of 5 and 4 should be 5
    p = root.left
    q = root.left.right.right
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val}: {lca.val} (Expected: 5)")
