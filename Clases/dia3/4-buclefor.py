# BUCLE FOR
# METODO TRADICIONAL
print("Forma Tradiciona")
print(1)
print(2)
print(3)
print(4)

print()

# METODO CON BUCLE FOR
# RANGE(v inicial, >(menor) al v final, incremento)
print("range(5)")
for contador in range(5):
    print(contador)

print()

print(range(2,5))
for contador in range(2,5):
    print(contador)
    
print()

print(range(1,50,10))
for contador in range(1,50,10):
    print(contador)

print()

print("Tabla de Multiplicar")
tabla = input("Ingrese el numero de la tabla: ")
for contador in range(1,13,1):
    print(f"{tabla} * {contador} = {int(tabla) * int(contador)}")
