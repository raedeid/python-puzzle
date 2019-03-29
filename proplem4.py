#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers
def both_way(a):#test if result of production is palindrome
    b=list(str(a))
    if b[:]==b[::-1]:#find if the number equal his inverse 
        return True
    return False

for c in range(10,100):#loop for 2 digit number 
    for d in range(100,1000):#loop for 3 digit number 
       production=c*d
       all_production=[]
       if both_way(production):
          all_production.append(production)#add the palindrome for all_production lis
          print(all_production)
