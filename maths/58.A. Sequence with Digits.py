
# for _ in range(int(input())):
#     a,k = map(int,input().split())
#     a = str(int(str(a)))
#     for _ in range(k-1):
#         a = int(a)+ int(max(a))*int(min(a))
#         a = str(a)
#         if min(a) == "0":
#             break
#     print(a)

def mul(x):
    m = 10
    n = 0
    while x>0:
        y = x%10
        x//=10
        x = int(x)
        m = min(m,y)
        n = max(n,y)
    return m*n

def main():
    for _ in range(int(input())):
        a,k = map(int,input().split())
        for _ in range(k-1):
            l =  mul(a)
            if l == 0:
                break
            a +=l
        print(a)

if __name__ == "__main__":
    main()


