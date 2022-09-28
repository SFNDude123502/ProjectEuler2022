import funcs as f
su=1
for i in [10,11,13,14,16,17,18,19]:
  for j in f.primeFactorization(i):
    su*=j
print(su)
