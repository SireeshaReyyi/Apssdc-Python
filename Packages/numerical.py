def isPrime(n):
    flag=1
    if n==2:
        return True
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                flag=0
                return False
        if flag==1:
            return True

def PrimeFactors(n):
    if isPrime(n):
        return 1
    c=0
    for i in range(2,n//2+1):
        if isPrime(i) and n%i==0:
            c=c+1
    return c

def highestRemainder(n):
    hr=0
    v=n
    for i in range(n-1,n//2,-1):
        r=n%i
        if r>hr:
            hr=r
            v=i
    print(v) 