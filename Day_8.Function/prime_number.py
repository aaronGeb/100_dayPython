#!/usr/bin/python3
def isPrime(n):
    if n< 2:
     
     return False
    i =2
    while i <= n/2: 
        if n%i==0:
            return False
        i +=1    
    return True        


for i in range(100):
    if isPrime(i):
        print(i,end=",")
    else:
        pass
print()