# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: 'Optional[TreeNode]'):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Example 1
    # Input
    # ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    # [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    # Output
    # [null, 3, 7, true, 9, true, 15, true, 20, false]
    
    # Constructing the tree: [7, 3, 15, null, null, 9, 20]
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    obj = BSTIterator(root)
    print(obj.next())    # return 3
    print(obj.next())    # return 7
    print(obj.hasNext()) # return True
    print(obj.next())    # return 9
    print(obj.hasNext()) # return True
    print(obj.next())    # return 15
    print(obj.hasNext()) # return True
    print(obj.next())    # return 20
    print(obj.hasNext()) # return False
