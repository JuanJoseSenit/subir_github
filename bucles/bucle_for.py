for i in ["juanjo",10, "Python"]:   #en python cuando defines i puede ser una lista, tupla, rango....
	print(i)

for i in ["juanjo",10, "Python"]:   
	print(i, end=" ") #para que no haga salto de linea en cada impresion

print("")

for i in "juanjo":  #si añadimos un string lo recorre letra por letra
	print(i)


if ".com" in "juanjo.senit@gmail.com":
	print("hola")

for i in range(5):  #es recorrer i desde 0 hasta 4. lo tipico de los bucles for de java
	print(i, end=" ")
print("")


#COMPROBACION DE DIRECCION DE CORREOS

direccion_correo=False

mi_correo=input("Introduzca su email: ")
for i in mi_correo:
	if i=="@":
		direccion_correo=True
if direccion_correo==True:
	print("Direccion correcta")
else:
	print("Direccion incorrecta")

	
