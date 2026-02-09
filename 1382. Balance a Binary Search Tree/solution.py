# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: In-order traversal to get nodes in sorted order
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST from sorted nodes
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            curr = nodes[mid]
            curr.left = build(l, mid - 1)
            curr.right = build(mid + 1, r)
            return curr
        
        return build(0, len(nodes) - 1)
