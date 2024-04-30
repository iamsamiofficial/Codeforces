for i in range(int(input())):
    x = input()

    print("cryeadn"[sum(map(int,x))%3 == 0 and x.count("0") and x.count("0")+x.count("2")+x.count("4")+x.count("6")+x.count("8")>1::2])