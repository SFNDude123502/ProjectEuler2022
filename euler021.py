import funcs as f
su=0
for i in range(1,10000):
    temp=0
    temp=f.sumDivisors(i)
    if f.sumDivisors(temp)==i and temp!=i:
        su=su+i+temp
        print(i)
        print(temp)
print(su/2)

