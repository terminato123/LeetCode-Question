# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        f=head
        while f is not None:
            arr.append(f.val)
            f=f.next
            b=0
            n=len(arr)
        for i in range(n):
            b=max(b,(arr[i]+arr[n-i-1]))
        return b
            
        