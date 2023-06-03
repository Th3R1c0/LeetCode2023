"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copylist = {None: None}
        curr = head
        while curr: 
            copylist[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr: 
            copy = copylist[curr]
            copy.next = copylist[curr.next]
            copy.random = copylist[curr.random]
            curr = curr.next
        return copylist[head]