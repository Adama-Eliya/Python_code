n = int(input("Entrer l'entier n :"))
i = 0
s = 0
while i != n:
	for j in range(2*n):
		if j%2 != 0:
			s = s + j**2
			i+= 1 # incrémentation de i après chaque somme

# affichage du résultat
print(f"la somme des {n} nombres impaire est :",s)
