#USO DEL CONTINUE
frase="juanjo es pro"
contador=0

for i in range(len(frase)):
	if frase[i]==" ":  #va a ir el ciclo leyendo letra por letra. si encuentra un espacio no hace nada, es decir, no entra en ningun if mas y no hace nada
		continue
	else:
		contador=contador+1
	print("hola")

print("La frase: " + frase + " contiene " + str(contador) + " letras ")


#USO DEL ELSE EN UN CICLO

direccion="juanjo_sv@hotmail.com"
for i in direccion:
	if i=="@":
		arroba=True
		break             #si encuentra una arroba inmediatamente para la ejecucion del ciclo, y como el else pertenece al for no entra

else:
	arroba=False
print(arroba)



direccion="juanjo_sv@hotmail.com"
for i in range(len(direccion)):
	if direccion[i]:
		arroba=True
		break             #si encuentra una arroba inmediatamente para la ejecucion del ciclo, y como el else pertenece al for no entra

else:
	arroba=False
print(arroba)