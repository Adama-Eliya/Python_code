a = int(input("entrer le premier nombre :"))
b = int(input("entrer le deuxieme nombre :"))
j = 1
s = 1
k = 1
for i in range(12):
    j+=1 
    if j== 2 or j % 2 !=0:
        if a % j ==0 and b %j == 0:
            s = s*j
        
   
if s == 1:
    print(f"le PGCD de ({a},{b}) est null ")
elif s== a:
    print(f"le PGCD de ({a},{b}) = {s}")
    print(f"le PGCD({a},{b})= {a} => {a}={b} ")
        
else :
    print(f"le PGCD de ({a},{b}) = {s}")    
              