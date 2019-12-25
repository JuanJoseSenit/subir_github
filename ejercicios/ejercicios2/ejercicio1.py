#NUMEROS IMPARES

for i in range(51):
	i=2*i-1
	if i<0:
		pass
	else:
		print (i, end=" ")

print(" ")

#NUMEROS IMPARES CREANDO UNA VARIABLE

for i in range(51):
	numero_impar=2*i-1
	if numero_impar<0:
		pass
	else:
		print(numero_impar,end=" ")

print(" ")



#NUMEROS IMPARES ESPECIFICANDO LOS SALTOS EN EL RANGO

for i in range(1,100,2):  #desde el 1 al 100 de dos en dos
	print(i, end=" ")


print(" ")

#NUMEROS IMPARES DE FORMA RESTO

for i in range(100):
	if i%2==0:
		pass
	else:
		print(i, end=" ")
