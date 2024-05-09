extends Node

var Entrada1 = true
var Entrada2 = true
var Salida : bool

func _ready():
	#Comienzo a preguntar
	if Entrada1==false and Entrada2==false:
		Salida = 0
		print("Primer if ",Salida)
	if Entrada1==false and Entrada2==true:
		Salida = 0
		print("Segundo if ", Salida)
	if Entrada1==true and Entrada2==false:
		Salida = 0
		print("Tercer if ", Salida)
	if Entrada1==true and Entrada2==true:
		Salida = 1
		print("Cuarto if ", Salida)

#CREAR LA TABLA PARA EL OR
