# !/usr/bin/python
# -*-coding: utf-8-*-


numero = 31
salir = False

while salir == False :
	
	if (numero % 7 == 0) or (numero % 7 == 1):
		J1 = "Ti"
	if (numero % 7 == 2) or (numero % 7 == 3) or (numero % 7 == 6):
		J1 = "Pi"
	if (numero % 7 == 4) or (numero % 7 == 5):
		J1 = "Pa"
	if (numero % 5 == 0) or (numero % 5 == 1) or (numero % 5 == 2):
		J2 = "Pa"
	if (numero % 5 == 3):
		J2 = "Ti"
	if (numero % 5 == 4):
		J2 = "Pi"
		

	if (J1 == "Pi" and J2 == "Ti"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J1"

	if (J1 == "Pa" and J2 == "Pi"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J1"

	if (J1 == "Ti" and J2 == "Pa"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J1"

	if (J2 == "Pi" and J1 == "Ti"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J2"

	if (J2 == "Pa" and J1 == "Pi"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J2"
  
	if (J2 == "Ti" and J1 == "Pa"):
		print numero , "J1 = ", J1, "y J2 = ", J2, " Gana J2"

	if ( J1 == J2):
		print numero ," Empate"

	if numero == 57 :
		
		salir = True
	
	numero = numero + 1
