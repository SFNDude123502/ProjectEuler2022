for a in range(1,333):
    for c in range(333,999):
        b=1000-(a+c)
        if a**2+b**2==c**2:
            print(a)
            print(b)
            print(c)
            print(a*b*c)
            break
