#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        a=[]
        k=len(price)
        for i in range(1,n+1):
            a.append(i)
        dp=[[0]*(n+1) for i in range(len(price)+1)]
        for i in range(n+1):
            dp[i][0]=0
        for j in range(n+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if a[i-1]<=j:
                    dp[i][j]=max((price[i-1]+dp[i][j-a[i-1]]),dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[k][n]
                
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends