n = input()
if len(n) == 1:
    if n == n.upper():
        print(n.lower())
    else:
        print(n.upper())
elif (n[0] == n[0].lower() and n[1:] == n[1:].upper()):
    s = n[0].upper()
    s+= n[1:].lower()
    print(s)
elif (n == n.upper()):
    print(n.lower())
else:
    print(n)