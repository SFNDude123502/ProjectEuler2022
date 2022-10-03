_p_nums=[]
c=0
while len(_p_nums)!=1000000:
    c+=1
    _p_nums.append(c*(1/2)*(3*c-1))
_p_set=set(_p_nums)
lrgi=0
lrgc=0
for i in range(500000,len(_p_nums)):
    c=0
    for j in range(len(_p_nums[:i])):
        if _p_nums[j]>_p_nums[i]/2:
            continue
        if _p_nums[i]-_p_nums[j] in _p_set:
            c+=1
    if c>lrgc:
        lrgi,lrgc=i,c
        print(i,c)
        if c>100:
            print(lrgi,lrgc)
            break
