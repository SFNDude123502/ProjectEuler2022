lisc=[]
for i in range(1234,9876):
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    seven=0
    eight=0
    nine=0
    zero=0
    temp=str(i)
    for j in range(len(temp)):
        if temp[j]=="1":
            one+=1 
            continue
        if temp[j]=="2":
            two+=1
            continue
        if temp[j]=="3":
            three+=1
            continue
        if temp[j]=="4":
            four+=1
            continue
        if temp[j]=="5":
            five+=1
            continue
        if temp[j]=="6":
            six+=1
            continue
        if temp[j]=="7":
            seven+=1
            continue
        if temp[j]=="8":
            eight+=1
            continue
        if temp[j]=="9":
            nine+=1
            continue
        if temp[j]=="0":
            zero+=1
            continue
    if  one!=2 and two!=2 and three!=2 and four!=2 and five!=2 and six!=2 and seven!=2 and eight!=2 and nine!=2 and zero==0:
        lisc.append(i)
su=0
for a in range(len(lisc)):
    for b in range(1,999):
        one=0
        two=0
        three=0
        four=0
        five=0
        six=0
        seven=0
        eight=0
        nine=0
        j=0
        temp=str(lisc[a])+str(b)+str(int(lisc[a]/b))
        if len(temp)!=9:
            continue
        for c in range(len(temp)):
            if temp[c]=="1":
                one+=1 
                continue
            if temp[c]=="2":
                two+=1
                continue
            if temp[c]=="3":
                three+=1
                continue
            if temp[c]=="4":
                four+=1
                continue
            if temp[c]=="5":
                five+=1
                continue
            if temp[c]=="6":
                six+=1
                continue
            if temp[c]=="7":
                seven+=1
                continue
            if temp[c]=="8":
                eight+=1
                continue
            if temp[c]=="9":
                nine+=1
                continue
        if one==1 and two==1 and three==1 and four==1 and five==1 and six==1 and seven==1 and eight==1 and nine==1:
            su+=lisc[a]
            su+=b
            su+=int(lisc[a]/b)
            print(lisc[a])
            print(temp)
            break
print(su)