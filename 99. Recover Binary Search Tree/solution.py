from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        You are given the root of a binary search tree (BST), where the values of exactly 
        two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
        
        Approach: Morris Traversal (O(1) space) or Inorder Traversal with tracking
        - In a valid BST, inorder traversal gives sorted values
        - We need to find the two nodes that are out of order
        - First wrong node: first node that is greater than its successor
        - Second wrong node: the successor (or last node that is smaller than predecessor)
        - Time: O(n), Space: O(h) for recursive approach
        """
        self.first = None   # First node to swap
        self.second = None  # Second node to swap
        self.prev = None    # Previous node in inorder traversal
        
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Check for violation
            if self.prev and self.prev.val > node.val:
                # If first violation, record both nodes
                if not self.first:
                    self.first = self.prev
                # Always update second (in case nodes are adjacent or not)
                self.second = node
            
            self.prev = node
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        
        # Swap the values of the two nodes
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val


# Helper function to build tree from list
def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to list representation for output."""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    
    return result


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: [1,3,null,null,2] -> [3,1,null,null,2]
    root1 = build_tree([1, 3, None, None, 2])
    print(f"Input: root = [1,3,null,null,2]")
    sol.recoverTree(root1)
    print(f"Output: {tree_to_list(root1)}")  # Expected: [3,1,null,null,2]
    
    # Example 2: [3,1,4,null,null,2] -> [2,1,4,null,null,3]
    root2 = build_tree([3, 1, 4, None, None, 2])
    print(f"\nInput: root = [3,1,4,null,null,2]")
    sol.recoverTree(root2)
    print(f"Output: {tree_to_list(root2)}")  # Expected: [2,1,4,null,null,3]
