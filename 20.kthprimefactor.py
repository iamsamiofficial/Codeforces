#User function Template for python3

class Solution:
    def kthPrime(self, n, k):
        # code here
        i = 2
        arr = []
        while (i*i <=n):
            while (n%i == 0):
                arr.append(i)
                n /= i
            i+=1
        if n >1:
            arr.append(n)
        return int(arr[k-1]) if k<=len(arr) else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.kthPrime(n, k))
# } Driver Code Ends