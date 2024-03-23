# Nombre mystère
import random
i = 5
x = random.randint(1,100)
print("😎😎*** le jeu du nombre mystère ***😎😎")
while i!= 0:
	print(f"Il te reste {i} essai{'s' if i>1 else ''}")
	y = input("Devine le nombre :")
	if y.isdigit():
		i-=1
		y = int(y)
		if y < x:
			print(f"le nombre mystère est plus grand que {y}")
		elif y > x :
			print(f"le nombre mystère est plus petit que {y}")
		else:
			print(f"Bravo ! le nombre mystère etait bien {x}")
			print(f"Tu as trouvé le nombre en {5 - i} essais")
			print("Fin du jeu.")
			break
	else:
		print("Veuiller entrer un nombre valide.")
		
if i == 0 and y != x:
    print(f"Dommage ! le nombre mystère etait {x}")
    print("Fin du jeu.")	

	


