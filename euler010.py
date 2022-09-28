import funcs as f
s=2
for i in range(3,2000000,2):
    if f.isPrime(i):
        s+=i
print(s)
