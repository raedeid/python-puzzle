#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divided(number):#check first 20 number 
    for a in range (2,21):
        if number%a!=0:
            return False
    return True
       

number=1
while True :#make loop to infinty number 
    if is_divided(number):# if the condation go on break and save last value 
        break
    number=number+1
    
print(number)


     
            
