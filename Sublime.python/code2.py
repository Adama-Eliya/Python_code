nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i%2 == 0]
print(nombres_pairs)
print("==============================================")
nombres = range(-10,10)
nombres_positifs = [i for i in nombres if i>= 0]
print(nombres_positifs)
print("==============================================")
nombres = range(5)
nombres_doubles = [i*2 for i in nombres]
print(nombres_doubles)
print("==============================================")
nombres = range(10)
nombres_inverse = [i if i %2 == 0 else -i for i in nombres]
print(nombres_inverse)