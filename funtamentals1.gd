extends Node

var numero1 = 20 #Variable Global
var numero2 = 40 #Variable Global
var lorenzo #Variable Global

func sumar() -> int:
	#Variable local
	var resultado = numero1 + numero2
	return resultado
	
func restar() -> int:
	var resultado = numero1 - numero2
	return resultado

func _ready():
	lorenzo = "Kevin"
	print(sumar())
	print(restar()) #Intentación (Indented) TAB
	#Concatenación de String con Int
	print("La suma es: ", sumar())
	#Concatenación de String con String
	print("Mi nombre es ... " + lorenzo)

#Genera una función para la Multiplicación y la División
#Imprime el resultado de la Multiplicación y la División
#Pero usa la Concatenación para imprimir los resultados
