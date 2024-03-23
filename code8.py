"""A = int(input("Entrer la valeur de A :"))
B = int(input("Entrer la valeur de  B :"))
C = A
A = B
B = C
print(f"la nouvel valeur de A est {A} et celle de B est {B}")"""

                    #OU

A = int(input("Entrer la valeur de A :"))
B = int(input("Entrer la valeur de  B :"))
A,B = B,A
print(f"la nouvel valeur de A est {A} et celle de B est {B}")