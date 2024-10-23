# ns = [1]
# mod = 10**8
# for i in range(2,mod+1):
#     ns.append((ns[-1]+((i*i)+(i*(i-1)))))



# for _ in range(int(input())):
#     n = int(input())
#     print((2022*(ns[n-1]))%((10**9)+7))
mod = (10**9+7)
for _ in range(int(input())):
    n = int(input())
    ns = (((n*(n+1))*(2*n+1))//6)+((((n*(n+1))*(2*n+1))//6)-((n*(n+1))//2))
    print((2022*ns)%mod)