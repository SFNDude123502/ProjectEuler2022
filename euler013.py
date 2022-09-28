nu = []
with open('ProjectEuler2022/euler013.txt', 'r') as f:
    for n in f:
        nu.append(int(n))
s=str(sum(nu))
print(s[0:10])
