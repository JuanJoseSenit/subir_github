print("EJERCICIO 3")
'''Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''

#FUNCIONES A EMPLEAR

def comprobar_longitud(palabra):
	longitud_palabra=len(palabra)
	while longitud_palabra<4:
		palabra=input("Recuerde que la palabra debe tener más de 3 letras. Introduzca palabra : ")
		palabra=palabra.upper()
		longitud_palabra=len(palabra)
	return palabra

def invertir_palabra(palabra):
	palabra_invertida=palabra[::-1]
	matriz=[]
	for i in range(len(palabra_invertida)):
		if i<3:
			matriz.append(palabra_invertida[i])
		else:
			continue
	return matriz


#PROGRAMA

palabra1=input("Introduzca palabra 1: ")
palabra1=palabra1.upper()
palabra1=comprobar_longitud(palabra1)


palabra2=input("Introduzca palabra 2: ")
palabra2=palabra2.upper()
palabra2=comprobar_longitud(palabra2)


palabra1_invertida=invertir_palabra(palabra1)   #son solo las ultimas tres letras de la palabra
palabra2_invertida=invertir_palabra(palabra2)  #son solo las ultimas tres letras de la palabra


contador=0
for i in range(len(palabra1_invertida)):
	if palabra1_invertida[i]==palabra2_invertida[i]:
		contador=contador+1
	else:
		continue

if contador==3:
	print("Rima total")
elif contador==2:
	print("Medio rima")
else:
	print("No rima")

