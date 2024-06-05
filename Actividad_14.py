import os
import msvcrt
import csv

clases = [("Levantamiento de pesas","Lunes y Martes de 8:30 a 10:00 a.m",20)]
reservas = []
usuarios = {}

while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")
    print("""\033[33m
    Sistema de gestión reservas FitLife
    ═══════════════════════════════════\033[0m
    1) Registrar nuevo usuario
    2) Reservar una clase
    3) Consultar clases disponibles
    4) Consultar reservas de un usuario
    5) Salir      """)
    opcion = int(input("Seleccione : "))

    if opcion==1:
        print("Regsitrar usuario")
        id = int(input("Ingrese su ID único: "))
        nom = input("Ingrese su nombre: ").capitalize
        if id in usuarios:
            print("\033[31mID en uso\033[0m")
        else:
            usuarios = {"id":id, "usuario":nom}
    elif opcion==2:
        print("Reservar una clase")
        id = int(input("Ingrese su ID único: "))
        if id in usuarios:
            res = input("Ingrese el nombre de la clase que desea reservar: ")
        else:
            print("\033[31mID no registrado\033[0m")
    elif opcion==3:
        print("Consultar clases disponibles")
        for c in clases:
            print(f"Clase: {clases[0]}")
    elif opcion==4:
        print("Consultar reservas de un usuario")
    elif opcion==5:
        print("Salir del programa")
        break