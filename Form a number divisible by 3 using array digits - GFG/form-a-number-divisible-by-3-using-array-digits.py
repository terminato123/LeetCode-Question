#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        s=""
        c=0
        for i in arr:
            s+=str(i)
        for a in s:
            c+=int(a)
        if c%3==0:
            return 1
        else:
            return 0
            
            
            
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends