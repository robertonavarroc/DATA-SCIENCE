# CALCULADORES

# ENTRADA
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
operacion = input("Ingrese la operacion +,-,*,/ : ")

# PROCESO
if  operacion == "+":
    resultado = numero1 + numero2 
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operacion no valida")
    exit()

#SALIDA
print(f"{numero1} {operacion} {numero2} = {resultado}")