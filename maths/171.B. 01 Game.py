for _ in range(int(input())):
    s = input()
    o = s.count("1")
    z = s.count("0")
    m = min(o,z)

    if m&1:
        print("DA")
        continue
    print("NET")