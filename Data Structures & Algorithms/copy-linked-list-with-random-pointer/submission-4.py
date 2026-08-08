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
        if head==None:
            return head
        curr=head
        while curr:
            temp_Node=Node(curr.val,next=curr.next)
            curr.next=temp_Node
            curr=curr.next.next
        curr=head
        while curr:
            if curr.random!=None:
                curr.next.random=curr.random.next
            else:
                curr.next.random=None
            curr=curr.next.next
        curr=head.next
        new_head=curr
        currp=head
        while curr.next:
            currp.next=curr.next
            curr.next=curr.next.next
            curr=curr.next
        currp.next=curr.next=None
        return new_head