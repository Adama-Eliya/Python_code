import math 
liste = []
liste2 = []
for x in range(int(input("entrer le nombre d'élève ds la salle :"))):
	nom = input("Entrer le nom de l'élève :")
	score = float(input("Entrer la note de l'élève :"))
	print("-"*20)
	liste1 = [nom,score]
	liste.extend(liste1) 
	liste2.append(score).sort()
	j = liste2[-2]
	for i in liste :
		if i == j:
			print(liste[i - 1])





	