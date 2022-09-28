def fib(a,b):
    global su
    print(a)
    _t=a+b
    i=b
    j=_t
    if su<=4000000: 
        su+=a
        fib(i,j)
su=0
m=0
n=1
fib(m,n)
print(su)