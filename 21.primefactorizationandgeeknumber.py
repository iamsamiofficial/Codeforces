#User function Template for python3

class Solution:
    def geekNumber(self, N):
        # code here
        i = 2
        arr = []
        
        while (i*i <=N):
            if N%i == 0:
                c = 0
                while (N%i==0):
                    c+=1
                    N /= i
                if c!=1:
                    return 0
            i+=1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        if ob.geekNumber(N)==1 :
            print("Yes");
        else :
            print("No");
# } Driver Code Ends