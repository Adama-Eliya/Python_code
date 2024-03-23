"""x = float(input("Veuiller entrer la longueur du rectangle :"))
y = float(input("Veuiller entrer la largueur du rectavngle :"))
print(f"le perimetre du rectangle est {(x + y)*2}m")
print(f"Et l'aire du rectangle est {x * y}m²")"""

#================================================================
              #ou
x = float(input("Veuiller entrer la longueur du rectangle :"))
y = float(input("Veuiller entrer la largueur du rectavngle :"))
s = (x + y)*2
t = x*y
print("le perimetre du rectangle est ",format(s,".2f"))
print("Et l'aire du rectangle est F",format(t,".2f"))