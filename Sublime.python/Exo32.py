"""Programme qui determine la somme que aura anna 
lors de son nième anniversaire"""
n = int(input("Entrer le nombre n : "))
s = 0
for i in range(1,n + 1):
	s = s + i*3 + 500
print(f"Amal aura {s}dh lors de son {n} ième anniversaire")