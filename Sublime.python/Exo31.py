""" Programme qui affiche les diviseurs d'un entier positif n"""
n = -1
while n <= 0:
	n = int(input("Entrer l'entier n :")) # nombre entrer par l'utilisateur
	for i in range(1,n + 1):
		if n % i == 0:
			print(i)
