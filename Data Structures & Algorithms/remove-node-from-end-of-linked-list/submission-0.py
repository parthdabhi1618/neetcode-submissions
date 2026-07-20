# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        Ncount=0
        curr=head
        while curr:
            curr=curr.next
            Ncount+=1
        dumm=ListNode()
        dumm.next=head
        prev=dumm
        curr=prev.next
        crit_num=Ncount-n
        while crit_num>0:
            prev=prev.next
            curr=curr.next
            crit_num-=1
        prev.next=curr.next
        return dumm.next
