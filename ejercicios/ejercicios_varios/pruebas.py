import random

def generar_numero_a_adivinar(longitud_numero):
	numero_menor_posible=pow(10,longitud_numero-1)
	
	numero_mayor_posible=(pow(10,longitud_numero)-1)

	numero_a_adivinar=random.randint(numero_menor_posible,numero_mayor_posible)
	
	print(numero_a_adivinar)
	return numero_a_adivinar

def comprobar_longitud_numero(adivinar_numero,longitud_numero):
	while len(adivinar_numero)!=longitud_numero:
		print("Recuerde que el numero que introduzca debe coincidir con la longitud del número")
		adivinar_numero=str(input("Intente adivinar el numero: "))
	return adivinar_numero




longitud_numero=str(input("Introduce la longitud del numero a adivinar: "))
longitud_numero=int(longitud_numero)

numero_a_adivinar=str(generar_numero_a_adivinar(longitud_numero))



adivinar_numero=-1 #para que entre en el ciclo while le doy un valor inicial

contador_global=0
while numero_a_adivinar!=adivinar_numero:
	contador=0
	
	adivinar_numero=str(input("Intente adivinar el numero: "))
	adivinar_numero=comprobar_longitud_numero(adivinar_numero,longitud_numero)

	for i in range(len(adivinar_numero)):
		if adivinar_numero[i]==numero_a_adivinar[i]:
			contador=contador+1	
		else:
			continue
	contador_global=contador_global+1
	print ("Con " + adivinar_numero + " has acertado " + str(contador) + " valores. Intente adivinar el número: ")

print("Con " + adivinar_numero + " has acertado " + str(contador) + " valores. Intente adivinar el número. FELICIDADES")
print("El número de intentos necesarios (sin introducir longitudes erróneas) para acertar ha sido de " + str(contador_global))























