#!/usr/bin/python
#importamos modulos basicos.
from colorama import Fore, init
init()
import time
import os

def switch():
	#funcion definida del menu de opciones.
	os.system('clear')
	print(Fore.GREEN)
	print("Hola, bienvenido a mi programa...")
	time.sleep(1)
	print(Fore.CYAN)
	print("Escoge una opcion: \n1- Encriptar Mensaje. \n2-Desencriptar Mensaje.")

while True:
	#Cuando sea verdadera la condicion, se cumplira un bucle del menu.
	switch()
	ask = int(input("\n>>> "))
	#primer condicional de nuestro programa.
	if ask==1:
		#input: se le preguntara el mensaje al usuario.
		message = str(input("Escribe aqui tu mensaje para Encriptar: "))
		translated = ""
		i = len(message)-1
		#Primer ciclo while, esto hara el proceso de encriptacion reversa en nuestro mensaje.
		while i>=0:
			translated= translated + message[i]
			i= i-1
		print(translated)
		print("Presione una tecla para continuar...")
		input()

	elif ask==2:
		#Segundo condicional de nuestro programa.
		message = str(input("Escribe aqui tu mensaje a Desencriptar: "))
		translated = ""
		i = len(message)-1
		#ciclo while para nuestra condicion, esto hara el proceso de desencriptacion reversa del mensaje.
		while i>=0:
			translated = translated+message[i]
			i = i - 1
		print(translated)
		print("Presione una tecla para continuar...")
		input()
