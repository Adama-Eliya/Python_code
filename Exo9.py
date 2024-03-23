a = int(input("veuiller entrer le nombre :"))
j = 0
s = 0
for i in range(8):
    j+=1 
    if j== 2 or j % 2 !=0:
        if a % j ==0 :
            s = s + j
if s == a:
    print("le nombre entier est parfait.")
else:
    print("le nombre entier n'est pas parfait.")                
       