import numpy as np


ch1 = np.array(['un gato amarillo', 'hamburguesa '], dtype=np.str)
ch2 = np.array([' un perro negro', ' hotdog'], dtype = np.str)

print("Array1:")
print(ch1)

print("Array2:")
print(ch2)

arrnew = np.char.add(ch1, ch2)

print("the new array is:")
print(arrnew)