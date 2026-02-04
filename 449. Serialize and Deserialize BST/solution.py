from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        vals = list(map(int, data.split()))
        
        def build(lower, upper):
            if not vals or not (lower < vals[0] < upper):
                return None
            
            root_val = vals.pop(0)
            root = TreeNode(root_val)
            root.left = build(lower, root_val)
            root.right = build(root_val, upper)
            return root
            
        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
