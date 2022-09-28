lisc=[]
for i in range(123456789,9876543210):
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
    if len(temp)==9:zero+=1
    #print("hi "+str(i))
    #print(one,two,three,four,five,six,seven,eight,nine,zero)
    if one==1 and two==1 and three==1 and four==1 and five==1 and six==1 and seven==1 and eight==1 and nine==1 and zero==1:
        lisc.append(i)
        print(i)
        if len(lisc)>1000100:
            print(lisc[999999])
            break
