# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumm=ListNode()
        dumm.next=head
        slow=dumm
        fast=slow
        while n>0:
            fast=fast.next
            n-=1
        prev_slow=slow
        while fast:
            prev_slow=slow
            slow=slow.next
            fast=fast.next
        prev_slow.next=slow.next
        return dumm.next