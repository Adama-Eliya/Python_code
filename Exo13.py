n = int(input("Veuiller entrer le nombre dont vous souhaitez calculer le factoriel :"))
# utilisons la boucle for
j,f = 0,1
for i in range(n):
    j+= 1
    f = f *j
print(f"factorielle de {n} ou {n}! : {f}")
# Utilisons la boucle while
while j < n:
    j+= 1
    f = f *j
print(f"factorielle de {n} ou {n}! : {f}")
    
        