set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#creacion de Set
set3 = set1 | set2
print(set3)
print(set1.union(set2))


# Creacion de Interseccion
set3 = set1 & set2
print(set3)
print(set1.intersection(set2))

# Creacion de Diferencia
set3 = set1 - set2
print(set3)
print(set1.difference(set2))

# Creacion de Diferencia simetrica
set3 = set1 ^ set2
print(set3)
print(set1.symmetric_difference(set2))

