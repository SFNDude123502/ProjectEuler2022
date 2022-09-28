
c=0
for i in range(1,1000000,2):
    if isPrime(i):
        c+=1
    if c==10001:
        print(i)
        break
