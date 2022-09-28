import funcs as f
c=0
lrgc=0
lrgi=0
for i in range(1,10000000):  
    s=i
    c=0
    while s!=4:
        if f.isEven(s):
            s/=2
            c+=1
        if f.isEven(s)==False:
            s=s*3+1
            c+=1
    if c>=lrgc:
        lrgc=c
        lrgi=i
        print(lrgi)
        print(lrgc)

print(lrgi)
print(lrgc)
