h,l = map(int,input().split())

#(a+h)2 = a2 + l2
#a2+2ah+h2 = a2+l2
#h2+2ah = l2
# a = (l2-h2)/2h

print(((l*l)-(h*h))/(2*h))
