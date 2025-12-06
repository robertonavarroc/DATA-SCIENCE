# LIBRERIA INTERNA DE PYTHON OS
import os

# CALCULADORA COMPLETA EN PYTHON
salir = "no"
while(salir=="no"):
    
    os.system("cls")
    
    # ENTRADA
    print("=========== CALCULADORA ============")
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
    print("=========== OPCIONES ============")
    print("1.- SUMA")
    print("2.- RESTA")
    print("3.- MULTIPLICACION")
    print("4.- DIVISION")
    operacion = input("Ingrese la opcion que desea : ")

    # PROCESO
    if  operacion == "1":
        resultado = numero1 + numero2 
        operacion = "+"
    elif operacion == "2":
        resultado = numero1 - numero2
        operacion = "-"
    elif operacion == "3":
        resultado = numero1 * numero2
        operacion = "*"
    elif operacion == "4":
        resultado = numero1 / numero2
        operacion = "/"
    else:
        print("Operacion no valida")
        
    #SALIDA
    print(f"{numero1} {operacion} {numero2} = {resultado}")
    
    salir = input("Desea salir: ")
    
    if salir == "si":
        break
    