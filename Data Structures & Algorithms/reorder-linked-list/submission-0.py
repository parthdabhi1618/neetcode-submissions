# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0
        curr=head
        while curr:
            n+=1
            curr=curr.next
        curr=head
        for i in range(n//2):
            curr=curr.next
        second_half=curr.next
        curr.next=None
        curr=second_half
        stack=[]
        while curr:
            stack.append(curr)
            curr=curr.next
        curr=head
        while stack:
            next_one=curr.next
            curr.next=stack.pop()
            curr=curr.next
            curr.next=next_one
            curr=curr.next