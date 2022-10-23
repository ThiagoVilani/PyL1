'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
#from Parcial-1.PP_STARWARS.funciones import buscador_personajes
import funciones
from funciones import exportar_archivo, lista_personajes
import re


def starwars_app():
    print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
    respuesta = input("Ingrese el numero de la opcion escogida")
    
    if(respuesta=="1"):
        print("1 - Listar los personajes ordenados por altura\n")
        lista_csv = funciones.listar_altura_peso(lista_personajes, "height")
        print(lista_csv)
    else:
        if (respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            lista_csv = funciones.encontrar_mas_altos(lista_personajes)
            print(lista_csv)
        else:
            if (respuesta=="3"):
                print("3 - Ordenar los personajes por peso\n")
                lista_csv = funciones.listar_altura_peso(lista_personajes, "mass")
                print(lista_csv)
            else:
                if (respuesta=="4"):
                    print("4 - Armar un buscador de personajes\n")
                    lista_csv = funciones.buscador_personajes(lista_personajes)
    
    while True:
        input_usuario = input("Desea exportar la lista a un archivo .csv?\n>>SI\n>>NO\n>>>")
        if re.search("si|no", input_usuario, re.IGNORECASE):
            input_usuario = input_usuario.lower()
            if input_usuario == "si":
                exportar_archivo(lista_csv)
            break

starwars_app()

