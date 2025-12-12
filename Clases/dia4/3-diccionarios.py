#DICCIONARIOS
#Son colecciones desornadas de elementos que se almacenan en pares clave-valor
#Cada clave es unica y se utiliza para acceder a su valor correspondiente.
#Se definen utilizandos llaves {} y los pares clave-valor se separa porn comas.

capitales = {
    "Peru":"Lima",
    "Ecuador":"Quito"
}

# Acceder al calor de la clave
print(capitales['Ecuador'])

# agregar o modificar valores forma1 
capitales['Ecuador'] = 'Colombia' 

# agregar o modificar valores forma2
nueva_capital = {
    "Bolivia":"La Paz"
}

capitales.update(nueva_capital)
print(capitales)

# Eliminar un par clave-valor
del capitales['Peru']
capital_eliminada = capitales.pop('Colombia','NO EXISTE')
print(f'Se elimino la capital {capital_eliminada}')
print(capitales)

#recorrer un diccionario
print("Recorriendo diccionarios")
# por claves
for clave in capitales.keys():
    print(clave)
    
# por valor
for valor in capitales.values():
    print(valor)
    
# por clave valor
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')
