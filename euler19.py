from calendar import c


def sun(day):
    return day%7==0
day=1
c=0
for i in range(1,101):
    day+=31
    if sun(day):
        c+=1
    if (1900+i)%4==0:
        day+=29
    else:
        day+=28
    if sun(day):
        c+=1
    day+=31
    if sun(day):
        c+=1
    day+=30
    if sun(day):
        c+=1
    day+=31
    if sun(day):
        c+=1
    day+=30
    if sun(day):
        c+=1
    day+=31
    if sun(day):
        c+=1
    day+=31
    if sun(day):
        c+=1
    day+=30
    if sun(day):
        c+=1
    day+=31
    if sun(day):
        c+=1
    day+=30
    if sun(day):
        c+=1
    if i==100:
        day+=30
    else:
        day+=31
        if sun(day):
            c+=1
    print(day)
    print(c-1)