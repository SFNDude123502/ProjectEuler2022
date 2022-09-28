import math
j=1
for i in range(1,101):
    j*=i
    print(i)
    print(j)
k=str(j)
su=0
for l in range(len(k)):
    su+=int(k[l])
print(su)