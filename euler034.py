def fact(su):
    t=1
    for i in range(su):
       t*=(i+1)
    return t
sum=0
for i in range(3,99999):
    su=0
    temp=str(i)
    for j in range(len(str(i))):
        su+=fact(int(temp[j]))
    if su==i:
        sum+=i
print(sum)
