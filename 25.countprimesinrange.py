#User function Template for python3

class Solution:
    def countPrimes(self,L,R):
        #code here
        arr = [True]*(R+1)
        
        arr [0] = arr[1] = False
        i = 2
        while (i*i<=R):
            if arr[i] == 1:
                j = i*i
                while (j<=R):
                    if (j%i) == 0:
                        arr[j] = False
                    j+=i
            i+=1
        primes = [num for num in range(max(2,L),R+1) if arr[num]]
        return len(primes)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.countPrimes(L,R)
        print(ans) 
# } Driver Code Ends