#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


def is_triple_of_Pythagorean(a,b,c):#check if the 3 number has feature of the pythagorean trriple
    if first**2+seconed**2==third**2:
        return True
    return False



for first in range(1,1000):#make roll for number under 1000 cause we need sumation equal 1000
    for seconed in range (first,1000):
        for third in range (seconed,1000):
            if first+seconed+third==1000:
                if is_triple_of_Pythagorean(first,seconed,third):
                    print (first*seconed*third)#print the product
                    break 

        
