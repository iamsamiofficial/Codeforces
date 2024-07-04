for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    com = list(zip(b,a))
    com.sort()
    ans = 1
    store = k
    while ans<n:
        for i in com:
            if i[0]<k:
                if (ans+i[1]>n):
                    store += (n-ans)*i[0]
                    ans+= (n-ans)
                    
                else:
                    ans+=i[1]
                    store+= i[0]*i[1]
            else:

                store += (n-ans)*k
                ans+=(n-ans)
                break
            if ans >=n:
                break
    print(store)