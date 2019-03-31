#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
import math
def is_prime(s): #this code for check the prime number
    for b in range (2,int(math.sqrt(s))+1):  #i used the sqrt cause check number contain the list of under s sqrt 
        if s%b==0 :
         return False 
    return True 

list_of_prime=[]
c=2 
while True:#mke infinty loop 
   if is_prime(c):
       list_of_prime.append(c)#check is the number prime
       if len(list_of_prime)>10001:#add number to lidt snd check if element of list under 10001
             break
   c=c+1

print(list_of_prime)
