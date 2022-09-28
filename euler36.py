import funcs as f

su=0
for i in range(1000000):
    if f.isPallendrome(str(i))!=True:
        continue
    if f.isPallendrome(f.base10to2(i))!=True:
        continue
    su+=i
print(su)        