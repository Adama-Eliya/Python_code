s,m= 0,0
n = int(input("Entrer le nombre d'entier dont vous souhaitez calculer la somme et la moyenne :"))
for i in range(n):
    x = int(input(f"nombre [{i + 1}] :"))
    s = s + x
m = s/n
print(f"la somme des nombre est",format(s))
print(f"la moyenne est ",format(m,".2f"))    
    