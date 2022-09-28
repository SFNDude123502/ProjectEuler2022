def sumDivisors(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum+=i
    return sum

def isPrime(num):
    if num<2: return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def quadratic(a,b,x):
    return (x**2+a*x+b)

def isEven(n):
    return n%2==0

def isPallendrome(nu: str):
    for i in range(len(nu)):
        if nu[i]!=nu[-(i+1)]:
            return False
    return True

def base10to2(nu):
    if(int(nu) <= 1):
        return nu
    bi = ''
    rem = int(nu)
    while rem > 0:
        bi = str(rem % 2) + bi
        rem = rem // 2    
    return bi