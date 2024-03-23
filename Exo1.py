x =int(input("Entrer la valeur de la premiere extrémité de l'interval :"))
y =int(input("Entrer la valeur de la seconde extrémité de l'interval :"))
t = int(input("Entrer la valeur à chercher dans l'interval :"))
if x <= t <= y :
    print(f"{t} est dans l'interval [{x},{y}]")
else:
    print(f"{t} n'est pas dans l'interval [{x},{y}]")    