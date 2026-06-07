from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        Construct a binary tree from the given 2D integer array descriptions.
        
        Approach:
        - We map node values (integers) to TreeNode objects using a hash map `nodes`.
        - We track child nodes using a set `children`.
        - For each description `[parent, child, isLeft]`:
          - We create the parent/child nodes if they don't exist yet.
          - We link child to the parent based on `isLeft`.
          - We add child to the `children` set.
        - The root node is the unique node that is in `nodes` but never as a child (not in `children` set).
        
        Complexity:
        - Time: O(N) where N is the length of descriptions.
        - Space: O(N) for nodes hash map and children set.
        """
        nodes = {}
        children = set()
        
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            children.add(child)
            
            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
                
        # The root is the node that has no parent
        for parent, _, _ in descriptions:
            if parent not in children:
                return nodes[parent]
        
        return None


# Helper function to serialize tree back to list for testing
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
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
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    descriptions1 = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    root1 = sol.createBinaryTree(descriptions1)
    output1 = tree_to_list(root1)
    print(f"Example 1 Output: {output1}")
    assert output1 == [50, 20, 80, 15, 17, 19], f"Test 1 Failed: {output1}"
    
    # Example 2
    descriptions2 = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    root2 = sol.createBinaryTree(descriptions2)
    output2 = tree_to_list(root2)
    print(f"Example 2 Output: {output2}")
    assert output2 == [1, 2, None, None, 3, 4], f"Test 2 Failed: {output2}"
    
    print("All tests passed successfully!")
