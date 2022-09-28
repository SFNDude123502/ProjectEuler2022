s=0
su=0
for i in range(1,101,1):
    s+=i**2
    su+=i
su=su**2
print(su-s)
