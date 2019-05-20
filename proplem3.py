#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
def prime(s): #this code for check the prime number
    for b in range (2,int(math.sqrt(s))+1):  #i used the sqrt cause check number contain the list of under s sqrt 
        if s%b==0 :
         return False 
    return True 


def largest_prime_factor(a):
    i=2
    prime_factor=[] 
    while i <=a/i :
        if prime (i) and a%i==0 : #to check if i is prime and factor for a
            prime_factor.append(i) 
            a/=i #try to division a to make code faster it will be lost of time if try to every single number
            if prime(a):
              prime_factor.append (a)
        else:
            i=i+1 
                
            
    return max(prime_factor) #this will return all prime factor

