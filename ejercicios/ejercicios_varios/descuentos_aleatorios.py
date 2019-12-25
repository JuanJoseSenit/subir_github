import random

#FUNCIONES A EMPLEAR

def comprobar_compra(compra_total):
	if compra_total<100:
		print("Su gasto es inferior a 100 $. No participa en la promoción")
		exit()

	else:
		print("Su gasto supera o iguala a 100 $. Participa en el concurso")
		return compra_total

def comprobar_bola_descuento(numero_aleatorio):
	if numero_aleatorio==0:
		bola=0
		print("Aleatoriamente usted obtuvo una bola blanca")
	elif numero_aleatorio==1:
		bola=10
		print("Aleatoriamente usted obtuvo una bola roja")
	elif numero_aleatorio==2:
		bola=20
		print("Aleatoriamente usted obtuvo una bola azul")
	elif numero_aleatorio==3:
		bola=25
		print("Aleatoriamente usted obtuvo una bola verde")
	elif numero_aleatorio==4:
		bola=50
		print("Aleatoriamente usted obtuvo una bola amarilla")
	return bola

def calcular_precio_rebajado(compra_total,descuento):
	precio_rebajado=(compra_total-((descuento/100)*compra_total))
	return precio_rebajado


#PROGRAMA
numero=0
while numero!=1:

	compra_total=float(input("Introduzca la cantidad total de compra: "))
	compra_total=comprobar_compra(compra_total)
	print(" ")

	numero_aleatorio=random.randint(0,4)


	descuento=comprobar_bola_descuento(numero_aleatorio)
	print(" ")
	print("Felicidades, ha ganado un " + str(descuento) + " % de descuento")

	nuevo_precio=calcular_precio_rebajado(compra_total,descuento)
	print(" ")
	print("Su nuevo total a pagar es de: " + str(nuevo_precio) + " $")
	print(" ")
	numero=int(input("Si desea salir presione 1. De lo contrario presione otro número: "))
print("Programa finalizado")






