def abd(a):
    su=0
    for i in range(1,int(a/2)+1):
        if a%i==0:
            su+=i
    return su

su=0
for i in range(28200):
    canbewritten=False
    for j in range(i):
        if abd(i-j)>(i-j) and abd(j)>j:
            canbewritten=True
    if canbewritten==False:
        su+=i
        print(i)
print(su)
