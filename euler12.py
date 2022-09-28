def euler12():
    se=0
    temp=0
    for i in range(1,1000000,1):
        se+=i
        temp=0
        for j in range(1,int(se/2)+1):
            if se%j==0:
                temp+=1
        print("Tri: "+str(i)+" Divis: "+str(temp))
        if temp>=500:
            print(se)
            return i

print(euler12())
