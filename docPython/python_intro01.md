> # Variables

```
print('Texto')
```
- Se utiliza para imprimir un texto cualquiera

```
print(nombre_variable)
```
- Se utiliza para imprimir un el valor de una variable

> #### Ejemplo 001
```
print('Texto', nombre_variable)

nombre = 'Roberto'
print('Hola', nombre)
```
- Se utiliza para imprimir un el valor de una variable
- :star: Resultado: `Hola Roberto`

```
input('texto')
```
- Se utiliza para solicitar al usuario que ingrese un valor

> #### Ejemplo 002
```
input('Cual es tu nombre?: ')

nombre2 = input('Cual es tu nombre?: ')
print('Hola', nombre2)
```
- `input` se utiliza decirle al usuario que ingrese un valor
- `print` Imprime el resultado
- :star: Resultado: `Hola nombre2`

<br>

---

<br>
<br>

> # Tipos de datos

```
#
```
- Se utiliza para escribir comentarios en pyhton

```
type(variable)
```
- Se utiliza para saber de que tipo de dato es la variable

```
print(`f`"{Variable1} {Variable2}")
```
- Utilizamos `f` dentro de un print, para poder imprimir variables
> **Ejemplo**

```   
numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))
operacion = input("Ingrese la operacion +/- : ")

if  operacion == "+":
    resultado = numero1 + numero2 
else:
    resultado = numero1 - numero2

#SALIDA
print(f"{numero1} {operacion} {numero2} = {resultado}")
```
- :star: Resultado: 5 + 5 = 10

---
<br>

> # Tipos de datos numericos
- Existen **3** tipos de datos numero en pyhton `int (enteros)`, `float (decimal)`, `complex (complejos)`

> ### **`int (entero)`**
- Tipo de dato numerico
```
Ejemplo:
    a = 5
    print(type(a))

    Resultado: <class 'int'>
```

> ### **`float (decimal)`**
- Tipo de dato decimal
```
Ejemplo:
    a = 10.5
    print(type(a))

    Resultado: <class 'float'>
```

> ### **`complex (complejos)`**
- Tipo de dato complejo, consta de una parte real y otra parte imaginaria
```
Ejemplo:
    a = (10.5 +/- 5f)
    print(type(a))

    Resultado: <class 'complex'>
```
