se=0
temp=0
for i in range(1,1000000):
    se+=i
    temp=0
    for j in range(1,int(se**.5)+1):
        if se%j==0:
            if se/j>se**.5:
                temp+=2
            else: 
                temp+=1
    if temp>=200: 
        print("Tri: "+str(i)+" Divis: "+str(temp))
    if temp>=500:
        print(i, se)
        break
