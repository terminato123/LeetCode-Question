# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        l=head
        c=0
        while t :
            t=t.next
            c+=1
        mid=c//2
        while mid:
            l=l.next
            mid-=1
        return l
        