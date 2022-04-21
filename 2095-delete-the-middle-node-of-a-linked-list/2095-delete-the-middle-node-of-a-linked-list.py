# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        d.next=head
        f=d
        s=d
        while f.next and f.next.next:
            f=f.next.next
            s=s.next
        s.next=s.next.next
        return d.next
            
        