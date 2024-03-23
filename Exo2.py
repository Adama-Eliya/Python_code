x = float(input("Entrer le premier nombre :"))
y = float(input("Entrer le second :"))
if x < 0 and y <0 :
    print("le produit de {} et {} est positif ".format(str(x),str(y)))
elif x >0 and y > 0:
    print("le produit de {} et {} est positif ".format(str(x),str(y)))
else:
    print("le produit de {} et {} est negatif ".format(str(x),str(y)))        