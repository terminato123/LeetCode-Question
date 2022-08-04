# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            n=prev = None
            cur=head  
            while cur!=None:
                n = cur.next
                cur.next= prev
                prev=cur
                cur=n
            head=prev
        return head