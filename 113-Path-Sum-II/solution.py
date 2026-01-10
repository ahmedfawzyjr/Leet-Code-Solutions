from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            current_path.append(node.val)
            current_sum += node.val
            
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(current_path))
            else:
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)
            
            current_path.pop()
            
        dfs(root, [], 0)
        return result

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
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    expected1 = [[5,4,11,2],[5,8,4,5]]
    result1 = solution.pathSum(root1, 22)
    # Sort to compare
    result1.sort()
    expected1.sort()
    assert result1 == expected1, f"Test case 1 failed: {result1}"
    print("Test case 1 passed")
    
    # Example 2
    root2 = build_tree([1,2,3])
    expected2 = []
    result2 = solution.pathSum(root2, 5)
    assert result2 == expected2, f"Test case 2 failed: {result2}"
    print("Test case 2 passed")
    
    # Example 3
    root3 = build_tree([1,2])
    expected3 = []
    result3 = solution.pathSum(root3, 0)
    assert result3 == expected3, f"Test case 3 failed: {result3}"
    print("Test case 3 passed")
    
    print("All test cases passed!")
