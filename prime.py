def prime(n):
    i=2
    while i<n//2:
        if n%i==0:
            return "not a prime number"
        
        i+=1
    return "prime number"    
n=int(input("enter the number"))
print(prime(n))            