# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
            return
        
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    def print_list(head):
        curr = head
        vals = []
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(vals))

    # Test Case 1: [4,5,1,9], node = 5
    head = ListNode(4)
    head.next = ListNode(5)
    node_to_delete = head.next
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    
    print("Original List:")
    print_list(head)
    
    sol = Solution()
    sol.deleteNode(node_to_delete)
    
    print("After deleting 5:")
    print_list(head)
    # Expected: 4 -> 1 -> 9
    
    # Test Case 2: [4,5,1,9], node = 1
    # Re-create list for simplicity or continue from previous state
    # Previous state: 4 -> 1 -> 9. Let's delete 1.
    node_to_delete = head.next # This is now the node with value 1
    
    sol.deleteNode(node_to_delete)
    print("After deleting 1:")
    print_list(head)
    # Expected: 4 -> 9
