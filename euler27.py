import funcs as f

_contenders=[]
for a in range(-999,1000):
    for b  in range(-1000,1001):
        _t=[]
        for n in range(1,11):
            if f.isPrime(f.quadratic(a,b,n)):
                _t.append(n)
            else:
                break
        if len(_t)>=10:
            _contenders.append([a,b])
            print(a,b,len(_t))
lis = _contenders
lrg=[0,0]
lrgc=0
for i in range(len(lis)):
    c=1
    while f.isPrime(f.quadratic(lis[i][0],lis[i][1],c)):
        c+=1
    if c>lrgc:
        lrgc=c
        lrg[0]=lis[i][0]
        lrg[1]=lis[i][1]
print(lrg, lrgc, lrg[0]*lrg[1])
