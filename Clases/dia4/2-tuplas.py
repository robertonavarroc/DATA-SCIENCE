# las tuplas son inmutables, no se puede agregar valores
dias=("Lunes","Martes","Miercoles","Jueves","Viernes")
print(f"Tipo de dato original: {type(dias)}")
#Para gregar nuevos valores a la tupla, lo convertimos en lista
dias = list(dias)
print(f"Tipo de dato original: {type(dias)}")
#Agregamos el valor a la lista
dias.append("Sabado")
#Lo volvemos a convertir en tupla
dias = tuple(dias)

print(dias)