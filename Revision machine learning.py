# les dictionnaires
dictionnaire = {
    "chien":"dog",
    "chat":"cat",
    "lapin":"rabbit",
    "tasse":"cup",
}
"""print(dictionnaire.keys())
print(dictionnaire.values())
print(dictionnaire["chat"])
print(dictionnaire.get('tauri'))
liste = ['eiozj','aiojzp','zoieiz','oizroz']
# methode fromkeys
print(dictionnaire.fromkeys(liste, 'default'))"""
# methode pop
print(dictionnaire.pop('tasse'))
print(dictionnaire)
for i,j in dictionnaire.items():
    print(i,":",j)
    
classeur = {
    "positif":[],
    "negatif":[],
    
}    
def trier(classeur, x) :
    if x >= 0:
        classeur['positif'].append(x)
    else:
        classeur['negatif'].append(x)
    return classeur       


print(trier(classeur, 5))        