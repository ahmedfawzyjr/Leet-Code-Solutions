# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two given nodes in a BST.
        
        Args:
            root: The root of the binary search tree.
            p: The first node.
            q: The second node.
            
        Returns:
            The lowest common ancestor node.
        """
        # Ensure p.val < q.val for simpler logic, though not strictly necessary if we check both bounds
        if p.val > q.val:
            p, q = q, p
            
        current = root
        while current:
            if current.val > q.val:
                # Both nodes are in the left subtree
                current = current.left
            elif current.val < p.val:
                # Both nodes are in the right subtree
                current = current.right
            else:
                # We have found the split point, or one of the nodes is the current node
                return current
        return None

if __name__ == "__main__":
    # Test Case 1
    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7  9
    #     / \
    #    3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    
    sol = Solution()
    
    # LCA of 2 and 8 should be 6
    p = root.left
    q = root.right
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val}: {lca.val} (Expected: 6)")
    
    # LCA of 2 and 4 should be 2
    p = root.left
    q = root.left.right
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val}: {lca.val} (Expected: 2)")
    
    # LCA of 3 and 5 should be 4
    p = root.left.right.left
    q = root.left.right.right
    lca = sol.lowestCommonAncestor(root, p, q)
    print(f"LCA of {p.val} and {q.val}: {lca.val} (Expected: 4)")
