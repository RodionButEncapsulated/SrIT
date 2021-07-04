# SrIT v0.01 Creado por __Rodion__

import time, os
from firebase import firebase

# Definiendo variables y constantes
firebase = firebase.FirebaseApplication("https://srit-76d6c-default-rtdb.firebaseio.com/", None)

fecha = time.strftime("%d/%m/%Y %H:%M:%S")
fecha = str(fecha)
registro = {}

LOGO = """
\t .d8888b.        8888888 88888888888 
\td88P  Y88b         888       888     
\tY88b.              888       888     
\t "Y888b.   888d888 888       888     
\t    "Y88b. 888P"   888       888     
\t      "888 888     888       888     
\tY88b  d88P 888     888       888     
\t "Y8888P"  888   8888888     888     
"""
INFO = """
[i] Software para Registro de Información y Tipificación.
[i] Creado por __Rodion__ (https://github.com/RodionButEncapsulated)
"""

# Definiendo funciones
def limpiarpantalla():
	os.system('clear') 

def menu():
	limpiarpantalla()
	print(LOGO)
	print(INFO)
	print("\tMenú Principal\n")
	print("[1] Crear Caso")
	print("[2] Mostrar Caso")
	print("[3] Borrar Caso")
	print("[0] Salir\n")

def registrarCaso():
	registro["nombre"] = input('Nombre: ')
	registro["documento"] = input('Documento: ')
	registro["extension"] = input('Extensión: ')
	registro["sede"] = input('Sede: ')
	registro["descripción"] = input('Descripción: ')
	registro["caso"] = input('Número de caso: ')
	registro["fecha"] = fecha
	
	firebase.post("/Registros_Casos/", registro)
	print(f"\nEl caso se registró con el número {registro['caso']}")

def mostrarCaso():
	casos_registrados = firebase.get("/Registros_Casos/", "")

	caso_a_buscar = input("[?] Ingrese el número de caso desea ver: ")

	limpiarpantalla()
	print(LOGO)
	print(INFO)

	for i in casos_registrados:
		if caso_a_buscar == casos_registrados[i]["caso"]:
			print("Número de Caso: " + casos_registrados[i]["caso"])
			print("Fecha de Creación: " + casos_registrados[i]["fecha"])
			print("Nombre: " + casos_registrados[i]["nombre"])
			print("Documento: " + casos_registrados[i]["documento"])
			print("Extension: " + casos_registrados[i]["extension"])
			print("Sede: " + casos_registrados[i]["sede"])
			print("Descripción: " + casos_registrados[i]["descripción"])

def borrarCaso():
	caso_a_borrar = input("[?] Ingrese el número de caso desea borrar: ")
	casos_registrados = firebase.get("/Registros_Casos/", "")

	for i in casos_registrados:
		if casos_registrados[i]["caso"] == caso_a_borrar:
			firebase.delete("/Registros_Casos/", i)
			print(f"El caso {caso_a_borrar} se borró correctamente.")

# Iniciando loop principal
while True:
	menu()
 
	opciónMenu = input("[?] Inserte una opción >> ")
 
	if opciónMenu == "1":
		limpiarpantalla()
		print(LOGO)
		print(INFO)
		print("\tRegistrar Caso\n")
		registrarCaso()
		input("\n[!] Presione 'Enter' para continuar.")

	elif opciónMenu == "2":
		limpiarpantalla()
		print(LOGO)
		print(INFO)
		print("\tMostrar Caso\n")
		mostrarCaso()
		input("\n[!] Presione 'Enter' para continuar.")

	elif opciónMenu == "3":
		limpiarpantalla()
		print(LOGO)
		print(INFO)
		print("\tBorrar Caso\n")
		borrarCaso()
		input("\n[!] Presione 'Enter' para continuar.")

	elif opciónMenu == "0":
		break

	else:
		print("")
		input("La opción no es correcta...\nPulsa una 'Enter' para continuar")