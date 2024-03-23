a = b = ""
while not(a.isdigit() and b.isdigit()):
    a = input("Entrer le premier nombre :")
    b = input("Entrer le deuxieme nombre :")
    if not(a.isdigit() and b.isdigit()):
    	print("veuiller des nombres valides")
print(f"le résultat de l'adition de {a} avec {b} est égale à {int(a) + int(b)}")	