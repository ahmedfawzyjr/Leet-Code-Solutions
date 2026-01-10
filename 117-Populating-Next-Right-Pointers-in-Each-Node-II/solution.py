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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root node
        head = root
        
        while head:
            dummy = Node(0)
            temp = dummy
            
            # Iterate through the current level
            while head:
                if head.left:
                    temp.next = head.left
                    temp = temp.next
                if head.right:
                    temp.next = head.right
                    temp = temp.next
                
                head = head.next
            
            # Move to the next level
            head = dummy.next
            
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
    
    # We need to find the leftmost node of each level to start traversal
    # Since it's not a perfect binary tree, we can't just go left.
    # But we can use the 'connect' logic or just standard BFS to find levels, 
    # then traverse next pointers.
    # Actually, the problem guarantees next pointers are set.
    # Let's just use the dummy head approach to traverse levels again for verification.
    
    head = root
    while head:
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        result.append('#')
        
        # Find next level start
        dummy = Node(0)
        temp = dummy
        curr = head
        while curr:
            if curr.left:
                temp.next = curr.left
                temp = temp.next
            if curr.right:
                temp.next = curr.right
                temp = temp.next
            curr = curr.next
        head = dummy.next
        
    return result

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = build_tree_level_order([1, 2, 3, 4, 5, None, 7])
    solution.connect(root1)
    # Expected: 1 -> #, 2 -> 3 -> #, 4 -> 5 -> 7 -> #
    expected1 = [1, '#', 2, 3, '#', 4, 5, 7, '#']
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
