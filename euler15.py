paths=1
for i in range(20):
    paths *= 40 - i
    paths /=i+1
print(paths)