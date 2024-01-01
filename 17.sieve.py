#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        arr = []
        store = []
        for i in range(N+1):
            arr.append(1)
        arr[0] = arr[1] = 0
        i = 2
        while (i*i <=N):
            if arr[i] == 1:
                j = i*i
                while (j<=N):
                    arr[j] = 0
                    j+=i
            i+=1
        for i in range(N+1):
            if arr[i] == 1:
                store.append(i)
        return store
    	
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends