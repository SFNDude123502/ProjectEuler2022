def euler7():
    lis=[]
    for i in range(1,1000000,2):
        pri=True
        for j in range(3,int((i/2)+2),2):
            if i%j==0:
                pri=False
            else:
                continue
        if pri:
            lis.append(i)
        if len(lis)>=10001:
            return lis[10000]
print(euler7())
