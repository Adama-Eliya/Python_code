liste = []
x = 0
while x != 5:
	print("choisissez parmi les 5 options suivantes :")
	print("1: Ajouter un élement à la liste")
	print("2: Retirer un élement de la liste")
	print("3: Afficher la liste")
	print("4: Vider la liste")
	print("5: Quitter")
	x = int(input("Votre choix :"))
	if x == 1:
		y = input("Entrer le nom de l'element à ajouter à la liste de courses:")
		liste.append(y)
		print(f"l'element {y} à été ajouté à la liste.")
		print("-----------------------------------------------")
	elif x == 3 :
		if len(liste)!= 0:
			print("Voici le contenu de Votre liste :")
			for i in range(len(liste)):
				print(f"{i + 1}.",liste[i])
		else:
			print("Votre liste ne contient aucun element.")
		print("-----------------------------------------------")
	elif x == 4 :
		liste.clear()
		print("la liste a été vidé de son contenu.")
		print("-----------------------------------------------")
	elif x == 2:
		t = input("Entrer le nom de l'element à retirer de la liste de courses :")
		if t in liste:
			liste.remove(t)
			print(f"l'element {t} a bien été supprimé de la liste.")
			print("-----------------------------------------------")
		else:
			print(f"l'element {t} n'est pas dans la liste.")
			print("-----------------------------------------------")

print("A bientôt !")

	

