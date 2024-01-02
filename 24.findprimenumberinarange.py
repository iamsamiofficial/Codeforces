#User function Template for python3

class Solution:        
    def primeRange(self,M,N):
        #code here
        arr = [1]*(N+1)
        arr[0] = arr[1] = 0
        i = 2
        while (i*i<=N):
            if arr[i] == 1:
                j = i*i
                while j<=N:
                    if j%i == 0:
                        arr[j] = 0
                    j+=i
            i+=1
            
        primes = [num for num in range(max(2,M),N+1) if arr[num] == 1]
        
        return primes
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends