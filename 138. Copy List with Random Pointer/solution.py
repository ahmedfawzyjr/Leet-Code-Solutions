from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create new nodes interleaved with original nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        # Step 2: Assign random pointers for new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the two lists
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            curr = curr.next
            
        return new_head

if __name__ == "__main__":
    solution = Solution()
    
    # Helper function to create list from array and return head
    def create_list(data):
        if not data:
            return None
        nodes = [Node(x[0]) for x in data]
        for i, x in enumerate(data):
            if i < len(data) - 1:
                nodes[i].next = nodes[i+1]
            if x[1] is not None:
                nodes[i].random = nodes[x[1]]
        return nodes[0]

    # Helper function to verify the copied list
    def verify_list(head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            if head1.random and head2.random:
                if head1.random.val != head2.random.val:
                    return False
            elif head1.random != head2.random:
                return False
            head1 = head1.next
            head2 = head2.next
        return head1 is None and head2 is None

    # Example 1
    data1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head1 = create_list(data1)
    copied1 = solution.copyRandomList(head1)
    assert verify_list(head1, copied1), "Test case 1 failed"
    print("Test case 1 passed")

    # Example 2
    data2 = [[1,1],[2,1]]
    head2 = create_list(data2)
    copied2 = solution.copyRandomList(head2)
    assert verify_list(head2, copied2), "Test case 2 failed"
    print("Test case 2 passed")

    # Example 3
    data3 = [[3,None],[3,0],[3,None]]
    head3 = create_list(data3)
    copied3 = solution.copyRandomList(head3)
    assert verify_list(head3, copied3), "Test case 3 failed"
    print("Test case 3 passed")
