def primeFactorization(nu):
  _facts=[]
  while nu%2==0:
    _facts.append(2)
  for i in range(3,int(nu**.5)+1,2):
    if nu%i==0:
      _facts.append(i)
      nu/=i
  if nu>2:
    _facts.append(nu)
  return _facts
su=1
for i in [10,11,13,14,16,17,18,19]:
  for j in primeFactorization(i):
    su*=j
print(su)
