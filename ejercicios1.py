print("Ejercicio 1")
# EJERCICIO #1
# Crea un programa que pida el nombre y la edad del usuario.
# El programa debera imprimir en que año el usuario cumplira 100 años
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print ("hola " + nombre + " tu edad es: " + str(edad))
print ("Cumpliras 100 años en: " + str(edad + 2020))

print("------------------------------------")
print("Ejercicio 2")

# EJERCICIO #2
# Crea un programa que pida un numero entero positivo y le haga saber al usuario si es par o primo
# (PISTA: investiga el operador modulo, denotado como % en muchos lenguajes de programacion)

num = int(input("Ingrese un numero entero positivo: "))
temp = num % 2
if (temp == 0):
    print("El numero " + str(num) + " es par")
else:
    print("El numero " + str(num) + " es impar")

print("-------------------------------------")
print("Ejercicio 3")


# Tome estas listas: 
# a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
# b = [1, 5, 77, 22, 90, 25, 83, 100, 02, 21, 90]
# y crea un programa que cree una nueva lista (o array)
# que contenga los elementos que NO se encuentran repetidos en ninguna de las dos lista anteriores
# y se imprima la lista completa (tambien se puede imprimir cada elemento de la lista)

a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 2, 21, 90]



print("----------------------------------")
print("Ejercicio 4")
# Crea un programa que le pida al usuario una palabra y muestre si esa palabra es un palindromo
# NOTA: un palindromo es una palabra que se puede escribir al derecho y al reves de la misma manera.
# (Por ejemplo: ana, ala, oso)
# (EXTRA: intenta hacerlo en 4 lineas de codigo solamente (investiga IF TERNARIO en Python))

word= input("Ingresa una palabra:\n")
wordl = list(word)
print("Es palindromo") if wordl == list(reversed(wordl)) else print("No es palindromo")

# el if ternario sirve para que la eleccion tenga dos caminos
#True if condicion False

print("----------------------------------")
print("Ejercicio 5")
# Crea un programa con un diccionario que contenga de llave un nombre
# y de valor el cumpleaños de esta persona.
# El programa pedira el nombre de la persona y se debera imprimir la fecha de su cumpleaños

diccionario = {'Uriel':'02/07/1996', 'Matt':'08/02/2000','Jorge':'01/09/1999'}
a = input("Ingrese un nombre: ")
print(diccionario[a])



#Un diccionario cuenta con una clave que lleva a un valor o valores en especificos 
#es de las pocas cosas que llevan llaves en pyton
#para poner varios datos ejemplo {'Matt': ['hola','balsoft']}
#Se puede agregar mas claves al diccionario sin ir hasta esa linea desde el codigo
#con el siguiente ejemplo:

#diccionario['Fernando'] = "29/05/200"
#a = input("Ingrese un nombre: ")

#se pueden usar comillas simples y dobles por igual en los diccionarios