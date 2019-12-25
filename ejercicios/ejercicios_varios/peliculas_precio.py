def comprobar_codigo(codigo):
	while codigo<=0 or codigo>=5:
		codigo=int(input("Recuerde que debe ser entre 0 y 4. Introduzca de nuevo el código: "))
	return codigo

def calcular_recargo(codigo,dias_retraso,diccionario_codigo_recargo):
	recargo_dia=diccionario_codigo_recargo[codigo]
	recargo_total=(recargo_dia*dias_retraso)
	return recargo_total

def calcular_total_pagar(precio_producto,recargo_total):
	return ((precio_producto+recargo_total))

print("CATEGORÍA		PRECIO 			CODIGO 			RECARGO 		" + "\nFAVORITOS		2.50$			  1				0.50$" + "\nNUEVOS			3.00$			  2			    0.75$" + "\nESTRENOS		3.50$			  3			    1.00$" + "\nSUPER ESTRENOS 	4.00$			  4			    1.50$")

numero=0
while numero!=1:
	codigo=int(input("Introduzca un código entre 1 y 4 correspondiente a la película: "))

	codigo=comprobar_codigo(codigo)

	diccionario_codigo_producto={1:2.5,2:3.0,3:3.5,4:4.0}

	precio_producto=diccionario_codigo_producto[codigo]

	diccionario_codigo_recargo={1:0.5,2:0.75,3:1.0,4:1.5}
	dias_retraso=int(input("Introduzca el número de dias de atraso en la devolución: "))

	recargo_total=calcular_recargo(codigo,dias_retraso,diccionario_codigo_recargo)

	total_pagar=calcular_total_pagar(precio_producto,recargo_total)
	print("El total a pagar es de: " + str(total_pagar) + "$")

	numero=int(input("Si desea salir presione 1. De lo contrario presione otro número: "))
print("Programa finalizado")