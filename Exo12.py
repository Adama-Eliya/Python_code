s,m,i,n= 0,0,0,0
while n != -1 :
    i += 1
    s = s + n
    n = float(input(f"note {i} : "))
    
m = s/(i - 1)    
print(f"la moyenne de ces {i - 1} notes : ",format(m,".2f"))    
    