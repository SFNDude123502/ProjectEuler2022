def euler10():
    s=2
    for i in range(3,2000000,2):
        ret=True
        for j in range(3,int((i**0.5)+2),2):
            if i%j==0:
                ret=False
        if ret:
            s+=i
    return s
print(euler10())
