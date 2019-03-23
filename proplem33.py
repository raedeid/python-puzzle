def prime(s):
    import math 
    s>=22
    for b in range (2,math.sqrt(s)+1):
        if s%b ==0 :
         return False 
    return True 


def largest_prime_factor(a):
    i=2
    prime_factor=[]
    while i <=a/i :
        if prime (i) and a%i==0:
            prime_factor.append(i)
            a/=i
        else:
            i=i+1 
                
            
    return(prime_factor)


