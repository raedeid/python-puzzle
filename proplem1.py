g=[]
for a in range (1000):
    if a%3==0 and a%5==0:
        g.append(a)
print(sum(g))        
