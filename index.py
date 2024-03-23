import random
u = 3
v = 40
vie_joueur = 50
vie_enemi = 50
while vie_joueur != 0 or vie_enemi != 0 :
	n = int(input("Souhaitez vous attaquer (1) ou utiliser une potion (2) : "))
	while n != 1 and n != 2:
			n = int(input("Souhaitez vous attaquer (1) ou utiliser une potion (2) : "))
	if n == 1:
		k = random.randint(5,10)
		z = random.randint(5,15)
		vie_joueur = vie_joueur - z
		vie_enemi = vie_enemi - k
		if vie_joueur < 0 :
			vie_joueur = 0
	
		elif vie_enemi < 0 :
			vie_enemi = 0
		
		print(f"Vous avez infligé {k} points de dégats à l'énémi ✂")
		print(f"l'énémi vous a infligé {z} points de dégats ⚒")
		print(f"Il vous reste {vie_joueur } points de vie.")
		print(f"Il reste {vie_enemi } points de vie à l'énémi.")
		print("-"*v)
		if vie_joueur == 0 or vie_enemi == 0:
			break

            
	else :
		u -=1
		if u != - 1:
			t = random.randint(15,50)
			p = random.randint(5,15)
			y = random.randint(5,15)

			print(f"Vous récupérer {t} points de vie ❤ ({u} 🧪 restant)")
			vie_joueur = vie_joueur + t
			print(f"l'énémi vous a infligé {y} points de dégats ⚒")
			vie_joueur = vie_joueur - y
			if vie_joueur <0:
				vie_joueur = 0
			print(f"Il vous reste {vie_joueur} points de vie.")
			print(f"Il reste {vie_enemi} points de vie à l'énémi.")
			print("-"*v)

			print("Vous passez votre tour ...")
			print("mine du joueur : 😋😁😝🤣")
			print(f"l'énémi vous a infligé {p} points de dégats ⚒")
			vie_joueur = vie_joueur - p
			if vie_joueur <0:
				vie_joueur = 0
			print(f"Il vous reste {vie_joueur} points de vie.")
			print(f"Il reste {vie_enemi} points de vie à l'énémi.")
			print("-"*v)
        
			
		else:
			print("Vous n'avez plus de potion 🧪")
        

    
if vie_joueur == 0:
		print("Vous avez echoué \n Fin du jeu ☹☹😭😭")
elif vie_enemi == 0:
	print("Bravo vous avez gagner \n Fin du jeu 🤑🎇🎆🎉🎉🎉🎊🎊")
