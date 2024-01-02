#User function Template for python3
import math
class Solution:
    def primeProduct (self, N):
        # code here
        i = 2
        arr = []
        while (i*i<=N):
            while (N%i == 0):
                arr.append(i)
                N/=i
            i+=1
        if N > 1:
            arr.append(N)
        ans = set(arr)
        final = 1
        for i in ans:
            final*=i
        return int(final)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.primeProduct(N))
# } Driver Code Ends