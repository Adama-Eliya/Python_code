j = 1
n = int(input("Veuiller entrer le nombre :"))
for i in range(n - 2):
    j += 1
    print(j)
    if n % j == 0:
        y = False
        break
    
if y == True :
    print("le nombre entier est premier")            
else:
    print("le nombre entier n'est pas premier")    