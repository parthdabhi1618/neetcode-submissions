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
        dummn=Node(0)
        dummn.next=head
        dummm=Node(0)
        add_to_pos=dict()
        pos_to_add=dict()
        currn,currm=dummn.next,dummm
        pos=1
        while currn:
            temp_Node=Node(currn.val)
            currm.next=temp_Node
            currm=currm.next
            add_to_pos[currn]=pos
            pos_to_add[pos]=currm
            currn=currn.next
            pos+=1
        currm.next=None
        currn=dummn.next
        currm=dummm.next
        while currn:
            if currn.random in add_to_pos:
                currm.random=pos_to_add[add_to_pos[currn.random]]
            currn=currn.next
            currm=currm.next
        return dummm.next
        