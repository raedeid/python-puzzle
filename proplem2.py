a=0
b=1
g=[]
while b<=4000000 :
    if b%2==0:
       g.append(b)
    a,b=b,a+b

print(sum(g))  
       
