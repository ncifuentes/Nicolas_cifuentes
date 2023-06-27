import numpy as np
import os
import time 


asientos = [[0] * 10 for _ in range (20)]

peliculas= {
    1:'Toy story 2'
}

precio_entrada = 3000

def mostrar_peliculas ():
    print("peliculas disponibles: ")
    for clave, pelicula in peliculas.items():
        print(f'{clave}. {pelicula}')
        opcion= input("Seleccione una opcion: " )
        print("Se ha seleccionado una pelicula ✔")
        print("Espere un momento...")
        time.sleep(5)
        os.system('csl')

def ver_asientos ():
    print("Estado de los asientos: ")
    for fila, asientos_fila in enumerate(asientos, start=1) 
        for col, estado in enumerate (asientos_fila, start=1)
        



print("Bienvenido Cliente")
nombre = input("Ingrese su nombre")
print("es alumno de Duoc?")
print("[1] Si ")
print("[2] No ")
opc_alumno = input("ingrese una respuesta")
if opc_alumno == 1:
    print("Bienvenido alumno")
elif opc_alumno == 2:
    print("Bienvenido cliente")

       

while True:
    print("Bienvenido a CineDuoc")
    print("[1] Peliculas en cartelera ")
    print("[2] Asientos disponibles ")
    print("[3] Listado de boletas ")
    print("[4] Comprar entrada ")
    print("[5] Salir ")
    opc= input("Elija la opcion deseada: " )
    
    if opc == 1:
       mostrar_peliculas()
    elif opc == 2:
        ver_asientos()



    


    