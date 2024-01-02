#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        i = 2
        arr = []
        while (i*i <=N):
            while N%i == 0:
                arr.append(i)
                N /= i
            i+=1
        if N >1:
            arr.append(N)
        return int(max(arr))
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends