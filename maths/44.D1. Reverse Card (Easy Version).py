
def gcd(a,b):
    if b == 0:
        return a

    return gcd(b,a%b)

def main():
    for _ in range(int(input())):
        p,q = map(int,input().split())
        final = []
        c = 0
        b = 1
        while b<=q:
            a = 1
            while a <= p:
                if gcd(a,b) == a:
                    c+=1
                a+=1
            b+=1
        final.append(c)
    return final
sam = main()
for i in sam:
    print(i) 