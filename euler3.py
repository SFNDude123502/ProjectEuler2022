ints=600851475143
lis=[]
inti=ints
while inti!=1:
    for i in range(ints-1,1,-1):
        if ints%i==0:
            lis.append(i)
            inti/=i
            break
print(lis)