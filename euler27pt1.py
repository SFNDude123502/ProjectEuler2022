import funcs as f

_contenders=[]
for a in range(-999,1000):
    for b  in range(-1000,1001):
        _t=[]
        for n in range(1,11):
            if f.isPrime(f.quadratic(a,b,n)):
                _t.append(n)
        if len(_t)>=10:
            _contenders.append([a,b])
            print(a,b,len(_t))
print(_contenders)