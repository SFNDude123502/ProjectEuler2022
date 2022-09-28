def sizeup(i):
    si=0
    l=lis[i]
    for j in range(len(l)):
        if l[j]=='A':
            si+=1
            continue
        if l[j]=='B':
            si+=2
            continue
        if l[j]=='C':
            si+=3
            continue
        if l[j]=='D':
            si+=4
            continue
        if l[j]=='E':
            si+=5
            continue
        if l[j]=='F':
            si+=6
            continue
        if l[j]=='G':
            si+=7
            continue
        if l[j]=='H':
            si+=8
            continue
        if l[j]=='I':
            si+=9
            continue
        if l[j]=='J':
            si+=10
            continue
        if l[j]=='K':
            si+=11
            continue
        if l[j]=='L':
            si+=12
            continue
        if l[j]=='M':
            si+=13
            continue
        if l[j]=='N':
            si+=14
            continue
        if l[j]=='O':
            si+=15
            continue
        if l[j]=='P':
            si+=16
            continue
        if l[j]=='Q':
            si+=17
            continue
        if l[j]=='R':
            si+=18
            continue
        if l[j]=='S':
            si+=19
            continue
        if l[j]=='T':
            si+=20
            continue
        if l[j]=='U':
            si+=21
            continue
        if l[j]=='V':
            si+=22
            continue
        if l[j]=='W':
            si+=23
            continue
        if l[j]=='X':
            si+=24
            continue
        if l[j]=='Y':
            si+=25
            continue
        if l[j]=='Z':
            si+=26
            continue
    return si

lis=open("euler22.txt").read().split(",")
lis = [x.replace('"', "") for x in lis]
lis.sort()
su=0
for i in range(len(lis)):
    temp=sizeup(i)
    t1=temp*(i+1)
    su+=t1
    print(su)
