#!/usr/bin/python

from colorama import Fore, init
init()
import time
import os

def switch():
	os.system('clear')
	print(Fore.GREEN)
	print("Hola, bienvenido a mi programa...")
	time.sleep(1)
	print(Fore.CYAN)
	print("Escoge una opcion: \n1- Encriptar Mensaje. \n2-Desencriptar Mensaje.")

while True:
	switch()
	ask = int(input("\n>>> "))
	if ask==1:
		message = str(input("Escribe aqui tu mensaje para Encriptar: "))
		translated = ""
		i = len(message)-1
		while i>=0:
			translated= translated + message[i]
			i= i-1
		print(translated)
		print("Presione una tecla para continuar...")
		input()

	elif ask==2:
		message = str(input("Escribe aqui tu mensaje a Desencriptar: "))
		translated = ""
		i = len(message)-1
		while i>=0:
			translated = translated+message[i]
			i = i - 1
		print(translated)
		print("Presione una tecla para continuar...")
		input()