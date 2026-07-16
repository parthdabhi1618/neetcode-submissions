# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_add=dict()
        idx=0
        while head:
            if not head in visited_add:
                visited_add[head]=idx
            else:
                return True
            idx+=1
            head=head.next
        return False