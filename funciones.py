"""
estructuras de una funcion en python
def nombre de la funcion (argumentos)
    operacion 
    operacion2
    return operacion 3
"""
"""
def saludo(nombre):
    print( "hola " + nombre + "!!")

nombre = input("ingrese tu nombre: ")
saludo(nombre)
"""
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
# def suma(numero1, numero2):
#     return numero1 + numero2

# def resta(numero1, numero2):
#     return numero1 - numero2

# print(resta(numero1,numero2))

"""
def resta(numero1=10, numero2=5):
    return numero1 - numero2

print(resta())
si no se manda ningun valor en este caso agarra de manera 
predeterminada los valores asignados en el def
"""
#-------------------------
# def posicional(*argumentos):
#     for arg in argumentos:
#         print(arg)

#     return None

# posicional(1 , "argumento posicional #2", [1,2,3,4,5] ,"args pos #4" )

#--------------------
"""
def nombre(**kwargs):
    for argumento in kwargs:
        # print(argumento)
        for valor in argumento: ("tambien funciona sin este ciclo por eso marca error")
            print(str(argumento) + " = " + str(kwargs[argumento]))

    return None
nombre(a=1, b="hola", c="adios", d=4.2)
"""

"""
pasar varios argumentos con o sin nombre
para los argumentos sin nombre, debera imprimir su valor
para los argumentos con nombre, debera imprimir el nombre y su valor

"""
combinacional =(nombre = "Matt", hola = "adios" ,345678, f=345,e)
def combinacional (*args, **zetas):
    suma = 0
    for arg in args:
        suma += arg
    print("suma= " + str(suma))
    
    for zeta in zetas
        print(str(zeta))

    return None