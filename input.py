import time
import sys
import os
s = "s"
n = "n"
os.system("title Mi primer programa, si")
def edad():
	ed = int (input ("Cual es su edad?:"))
	if ed>=18:
		print("Prosiga")
		time.sleep(2)
		os.system("cls")
		siono()
	else:
		print("Debe tener una edad mayor a 18 para poder utilizar este programa.")
		print("Cerrando...")
		time.sleep(4)
		quit()
def siono():
	r = input("Desea seguir?(S/N):")
	if r=="s":
		print("Ok")
		time.sleep(2)
		edad()
	if r=="n":
		print("Cerrando programa...")
		time.sleep(5)
		quit()
edad()











