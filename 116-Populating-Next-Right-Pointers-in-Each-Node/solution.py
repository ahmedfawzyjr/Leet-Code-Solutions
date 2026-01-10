from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        # Start with the root node
        leftmost = root
        
        # Iterate level by level
        while leftmost.left:
            head = leftmost
            while head:
                # Connection 1: connect left child to right child
                head.left.next = head.right
                
                # Connection 2: connect right child to next node's left child
                if head.next:
                    head.right.next = head.next.left
                
                # Move to next node in the current level
                head = head.next
            
            # Move to the next level
            leftmost = leftmost.left
            
        return root

def build_tree_level_order(values: list) -> Optional[Node]:
    if not values:
        return None
    
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
        
    return root

def check_next_pointers(root: Optional[Node]) -> list:
    # Traverse the tree level by level using the next pointers
    result = []
    leftmost = root
    while leftmost:
        curr = leftmost
        while curr:
            result.append(curr.val)
            curr = curr.next
        result.append('#')
        leftmost = leftmost.left
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = build_tree_level_order([1, 2, 3, 4, 5, 6, 7])
    solution.connect(root1)
    # Expected output format is serialized level by level with next pointers
    # But for verification we can check the next pointers traversal
    # Level 1: 1 -> #
    # Level 2: 2 -> 3 -> #
    # Level 3: 4 -> 5 -> 6 -> 7 -> #
    expected1 = [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']
    result1 = check_next_pointers(root1)
    print(f"Test Case 1: Expected {expected1}, Got {result1}")
    assert result1 == expected1
    
    # Example 2
    root2 = build_tree_level_order([])
    solution.connect(root2)
    expected2 = []
    result2 = check_next_pointers(root2)
    print(f"Test Case 2: Expected {expected2}, Got {result2}")
    assert result2 == expected2
    
    print("All test cases passed!")
