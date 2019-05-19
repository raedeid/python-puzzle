def both_way(a):#test if result of production is palindrome
    b=list(str(a))
    if b[:]==b[::-1]:#find if the number equal his inverse
        return True
    return False


g=[]
for c in range(999,99,-1):#loop for 2 digit number
    for d in range(999,99,-1):#loop for 3 digit number
       production=c*d
       if both_way(production):
          g.append(production)
          break  

print(max(g))
