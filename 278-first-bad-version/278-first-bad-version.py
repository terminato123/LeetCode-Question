# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        h=n
        while (l<=h):
            mid=(l+h)//2
            if isBadVersion(mid) and  not isBadVersion(mid-1):
                return mid
            if isBadVersion(mid):
                h=mid-1
            else:
                l=mid+1
        return l
        