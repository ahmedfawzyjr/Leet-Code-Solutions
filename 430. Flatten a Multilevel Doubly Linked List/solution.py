from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def flatten_dfs(node):
            curr = node
            last = node
            while curr:
                nxt = curr.next
                if curr.child:
                    child_head = curr.child
                    child_tail = flatten_dfs(curr.child)
                    
                    # Connect curr to child_head
                    curr.next = child_head
                    child_head.prev = curr
                    
                    # Connect child_tail to nxt
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail
                    
                    # Set child to None
                    curr.child = None
                    last = child_tail
                else:
                    last = curr
                curr = nxt
            return last
        
        flatten_dfs(head)
        return head
