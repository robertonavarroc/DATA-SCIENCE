dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

#recuperar info de la lista
print(dias[0])

print()

#Mostrar todos los valores de la lista
for contador in range(0,5):
    print(dias[contador])
    
print()

#Agregar elementos a la lista
dias.append("Sabado")
dias.append("Domingo")

#Mostrar todos los valores de la lista forma 2
for dia in dias:
    print(dia)

print()
    
#Eliminar elementos de la lista 1 solo valor
dias.pop(6)

#Eliminar por rango
del dias[0:2]

#Mostrar todos los valores de la lista forma 2
for dia in dias:
    print(dia)
    
print()

#Cambiar valor de la lista
dias[0] = "Lunes"

#Mostrar todos los valores de la lista forma 2
for dia in dias:
    print(dia)