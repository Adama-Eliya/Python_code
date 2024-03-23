"""x = float(input("Donner la valeur de x :"))
y = float(input("Donner la valeur de y :"))
somme = x + y
soustraction = x - y
produit = x *y
if y != 0:
    division = x/y
    print(f"la division de {x} et de {y} = {division}")
else:
    print("la division est impossible veuiller saisir une autre valeur de y")
print(f"la somme de {x} et de {y} = {somme}") 
print(f"le produit de {x} et de {y} = {produit}")   
print(f"la soustration de {x} et de {y} = {soustraction}")"""


x = float(input("Donner la valeur de x :"))
y = float(input("Donner la valeur de y :"))
somme = x + y
soustraction = x - y
produit = x *y
if y != 0:
    division = x/y
    print("la division est = ",format(division,".2f"))
else:
    print("la division est impossible veuiller saisir une autre valeur de y")
print(f"la somme est = ",format(somme,".2f")) 
print(f"le produit est = ",format(produit,".2f"))   
print(f"la soustration est = ",format(soustraction,".2f"))                             