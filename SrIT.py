# Cambiado el nombre del archivo
import time

fecha = time.strftime("%d/%m/%Y %H:%M:%S")
fecha = str(fecha)
registro={}
escribir=''

print(fecha)
print(fecha.split(' '))
print('')

while True:
	nombre = input('Nombre: ')
	documento = input('Documento: ')
	extension = input('Extensión: ')
	sede = input('Sede: ')
	descripcion = input('Descripción: ')
	caso = input('Número de caso: ')
	
	escribir+=f'Caso: #{caso}\nNombre: {nombre}\nDocumento: {documento}\nExtensión: {extension}\nSede: {sede}\nDescripción: {descripcion}\n\n'
	
#	with open(f'{fecha}.txt','w') as file:
#		file.write(escribir)
#		print('')
		
	file = open(f'{fecha}.txt','w')
	file.write(escribir)
	print('')
	file.close
