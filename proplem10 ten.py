#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
import math
def is_prime(number):
    for b in range(2,int(math.sqrt(number))+1):
        if number%b==0:
            return False
    return True


list_of_primes=[]
for Number in range(2,2000000):
    if is_prime(Number):
        list_of_primes.append(Number)



print(sum(list_of_primes))        

