h1,m1 = map(int,input().split(":"))
h2,m2 = map(int,input().split(":"))

mh1 = (h1*60)+m1
mh2 = (h2*60)+m2
midh = (mh1+mh2)//2
h = midh//60
m = midh%60

if h<=9 and m<=9:
    print("0",h,":","0",m,sep="")
elif h<=9:
    print("0",h,":",m,sep="")
elif m<=9:
    print(h,":","0",m,sep="")
else:
    print(h,":",m,sep="")

