import funcs as f
def cycle(denom :int, num :int=1)->int:
    reminders = []
    rems = None
    while rems not in reminders:
        reminders.append(rems)
        num *= 10
        rems = num % denom
    reminders.pop(0)
    return len(reminders)
pns=[]
for i in range(2,1000):
    if f.isPrime(i):
        pns.append(i)
lrgc=0
for j in pns:
    if cycle(j) >lrgc:
        lrgc=cycle(j)
        print(j, lrgc)

