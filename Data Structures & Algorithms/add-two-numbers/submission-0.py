# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def _int_to_rev_ll(intval):
    head=ListNode('#')
    curr=head
    for ch in str(intval)[::-1]:
        temp_Node=ListNode(int(ch))
        curr.next=temp_Node
        curr=curr.next
    curr.next=None
    return head

def _rev_ll_to_int(head):
    curr=head
    f_str=''
    while curr:
        f_str=str(curr.val)+f_str
        curr=curr.next
    return int(f_str)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=_rev_ll_to_int(l1)
        b=_rev_ll_to_int(l2)
        head=_int_to_rev_ll(a+b).next
        return head