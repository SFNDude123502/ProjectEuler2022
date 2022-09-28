import funcs as f
lis=[]
for i in range(999,700,-1):
    for j in range(999,700,-1):
        bar=str(i*j)
        if len(bar)%6==0:
            if f.isPallendrome(bar):
                print(i*j)
                lis.append(bar)
print(max(lis))
