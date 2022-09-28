import funcs as f
for i in range(2,int(600851475143**.5)+1):
    if 600851475143%i==0:
        if f.isPrime(i):
            print(i)
