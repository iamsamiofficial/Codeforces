for _ in range(int(input())):
    w,h = input().split()
    w = int(w)
    h = int(h)
    l1 = input().split()
    l2 = input().split()
    l3 = input().split()
    l4 = input().split()
    ans = []
    ans.append((int(l1[-1])-int(l1[1]))*h)
    ans.append((int(l2[-1])-int(l2[1]))*h)
    ans.append((int(l3[-1])-int(l3[1]))*w)
    ans.append((int(l4[-1])-int(l4[1]))*w)
    print(max(ans))