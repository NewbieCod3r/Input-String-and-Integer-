# Importacion de libererias/Libraries import
import time # Libreria para "time.sleep()"/Library for "time.sleep()"
import os # Libreria para "os.system"/Library for "os.system"
import platform
import sys
from time import sleep # de time importar sleep"/of time, import sleep
# Creacion de variables
# Creation of variables
s = "s"
n = "n"
eng = "eng"
esp = "esp"
sys = platform.system() # variable for Detect OS
# Funciones y codigo
# Functions and Code
def languague():
	print("   =================")
	print("""
    * English (eng)*
    * Spanish (esp)*
		""")
	print("   =================")
	sl = input("Select languague:")
	if sl=="esp":
		os.system("cls")
		espp()

def espp():
	if sys=='Windows':
		os.system("title Mi primer programa, si") #Titulo de consola con comando de cmd/Console title with cmd command
		edad()
	else:
		edad()

def edad(): # Creacion de funcion "edad"
	ed = int (input ("Cual es su edad?:")) # Creacion de variable ed con input int dentro para usar input con integers 
	if ed>=18: # Si la variable "ed" es mayor o igual que 18 realizar:
		print("Prosiga") # Mostrar en pantalla "Prosiga"
		sleep(2) # Tiempo de espera de 2s
		os.system("cls") # Borrar pantalla de la terminal con comando de cmd
		siono() # Iniciar la funcion "Siono"
	else: # Si la condicion no se cumple, realizar:
		print("Debe tener una edad mayor a 18 para poder utilizar este programa.") # Mostrar en pantalla "Debe tener una edad mayor a 18 para poder utilizar este programa."
		print("Cerrando...") # Mostrar en pantalla "Cerrando..."
		sleep(4) # Tiempo de espera de 4s/Delay of 4s
		quit() # Salir/Quit
def siono(): # Creacion de funcion "Siono"
	r = input("Desea seguir?(S/N):") # Creacion de variable r con input dentro
	if r=="s": # Si r es igual a "s" realizar:
		print("Ok") # Mostrar en pantalla "ok"
		sleep(2) # Tiempo de espera de 2s
		edad() # Iniciar la funcion "edad"
	if r=="n": # Si r es igual a "n" realizar:
		print("Cerrando programa...") # Mostrar en pantalla "Cerrando programa..."
		sleep(5) # Tiempo de espera de 5s
		quit() # Salir
languague()
