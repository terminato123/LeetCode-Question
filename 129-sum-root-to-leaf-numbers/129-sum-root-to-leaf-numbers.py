# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        pathsum=0
        def helper(root,pathsum):
            if root is None:
                return 0
            pathsum=pathsum*10+root.val
            if root.left==None and root.right==None:
                return pathsum
            return helper(root.left,pathsum)+helper(root.right,pathsum)
        return helper(root,pathsum)
            
        