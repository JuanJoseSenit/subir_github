print("EJERCICIO 4")
'''Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). 
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.'''


#FUNCIONES A EMPLEAR

def comprobar_anno(anno):
	while anno<0:
		anno=str(input("Recuerde que el año debe ser positivo.Introduzca a cuantos años quiere calcular el capital: "))
		anno=float(anno)
	return anno

def calcular_capital(capital,interes,anno):
	parentesis=(1+(interes/100))
	capital_estimado=(capital*(pow(parentesis,anno)))
	return capital_estimado

#PROGRAMA

capital=str(input("Introduzca capital actual ($): "))
capital=float(capital)

interes=str(input("Introduzca un tipo de interés (%): "))
interes=float(interes)

anno=str(input("Introduzca a cuantos años quiere calcular el capital: "))
anno=float(anno)
anno=comprobar_anno(anno)

capital_estimado=calcular_capital(capital,interes,anno)

print("El capital será de : " + str(capital_estimado) + " $")

