numero1=float(input("Introduzca el primer numero: "))
numero2=float(input("Introduzca el segundo numero: "))

def DevuelveMaximo(numero1,numero2):
	if numero2>numero1:
		return numero2
	elif numero2<numero1:
		return numero1
	else:
		print("Son iguales")
		return numero1

print ("El número mayor es : " + str(DevuelveMaximo(numero1,numero2)))   #para concatenar en python es necesario pasar los numeros a str porque es un lenguaje altamente cifrado