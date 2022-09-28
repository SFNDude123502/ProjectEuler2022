import funcs as f
c=1
for i in range(3,1000000,2):
    if f.isPrime(i):
        c+=1
    if c==10001:
        print(i)
        break
