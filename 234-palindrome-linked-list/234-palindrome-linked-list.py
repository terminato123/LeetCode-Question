# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        if head is None:
            return False
        else:
            temp=head
            while temp:
                a.append(temp.val)
                temp=temp.next
        if a[:]==a[::-1]:
            return True
        else:
            return False
        