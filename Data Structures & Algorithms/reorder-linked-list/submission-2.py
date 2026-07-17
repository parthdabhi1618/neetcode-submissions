# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def _reverse_linkedlist(head):
    if not head:
        return head
    prev=head
    curr=prev.next
    prev.next=None
    while curr:
        next_one=curr.next
        curr.next=prev
        prev=curr
        curr=next_one
    head=prev
    return head

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:      
        if not head:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None #End
        rsh=_reverse_linkedlist(second_half)
        curr=head
        while rsh:
            next_curr=curr.next
            curr.next=rsh
            next_rsh=rsh.next
            rsh.next=next_curr
            curr=next_curr
            rsh=next_rsh