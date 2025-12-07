# RETO 1 : CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA 
# QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
# POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES 
# DEBERIA MOSTRARME SU VALOR EN DOLARES QUE SERIA 1000 DOLARES CONSIDERANDO 
# QUE EL TIPO DE CAMBIO ES 3

import os
import time

salir = "si"

while salir == "si":
    os.system("cls")
    
    print("======== [TIPO DE CAMBIO] ===========")
    print("======== Tipo de cambio 3.0 =========")
    print("=====================================")
    moneda = round(float(input("Ingrese el monto a cambiar: ")),2)
    
    print("========== [OPCIONES] =============")
    print("1.- SOLES A DOLARES")
    print("2.- DOLARES A SOLES")
    print("3.- SALIR")
    opcion = input("Ingresar opcion: ")
    
    if opcion == "1":
        cambio = float(moneda / 3)
        print(f"{moneda} de soles a dolares: {round(cambio,2)}")
    elif opcion == "2":
        cambio = float(moneda * 3)
        print(f"{moneda} de dolares a soles: {round(cambio,2)}")
    elif opcion == "3":
        print("Programa Finalizado")
        break
    else:
        print("Opcion Invalida")
        salir = input("Deseas volver a intentarlo si/no: ").lower()
        
        if  salir == "no":
            break
        
    time.sleep(2)