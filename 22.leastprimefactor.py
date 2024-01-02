#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        # code here
        arr = []
        for i in range(n+1):
            arr.append(i)
        
        i = 2
        while (i*i <=n):
            j = i*i
            while j <=n:
                arr[j]%i == 0
                arr[j] = min(i,arr[j])
                j+=i
            i+=1
        return arr
                    
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends