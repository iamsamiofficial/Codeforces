for x in range(int(input())) :
   input()
   s=input()
   p =[]
   c =[]
   for y,k in enumerate(s) :
      if k not in c :
        p.append(len(set(s[:y+1]))+len(set(s[y+1:])))
        c.append(k)
   print(max(p))