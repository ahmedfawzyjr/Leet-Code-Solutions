from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        1. First, calculate the total sum of the tree.
        2. Then, for each subtree, calculate product = subtree_sum * (total - subtree_sum)
        3. Return the maximum product modulo 10^9 + 7.
        
        Time: O(n) - two passes through the tree
        Space: O(h) - recursion stack, where h is the height
        """
        MOD = 10**9 + 7
        subtree_sums = []
        
        def get_sum(node: Optional[TreeNode]) -> int:
            """Calculate subtree sum and store all subtree sums."""
            if not node:
                return 0
            
            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            subtree_sums.append(current_sum)
            return current_sum
        
        total_sum = get_sum(root)
        
        # Find maximum product
        max_product = 0
        for subtree_sum in subtree_sums:
            product = subtree_sum * (total_sum - subtree_sum)
            max_product = max(max_product, product)
        
        return max_product % MOD


# Helper function to build tree from list
def build_tree(values: list) -> Optional[TreeNode]:
    if not values:
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


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    root1 = build_tree([1, 2, 3, 4, 5, 6])
    print(f"Test 1: {sol.maxProduct(root1)}")  # Expected: 110
    
    # Test case 2
    root2 = build_tree([1, None, 2, 3, 4, None, None, 5, 6])
    print(f"Test 2: {sol.maxProduct(root2)}")  # Expected: 90
