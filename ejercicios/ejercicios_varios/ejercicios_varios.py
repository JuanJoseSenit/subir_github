
print("ejercicio 1")
#1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def funcion_max(num1,num2):
	if num1>num2:
		return num1
	if num1<num2:
		return num2

print(funcion_max(5,2))

print("ejercicio 2")

#2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_de_tres(num1,num2,num3):
	if num3>num2 and num2>num1:
		return num3
	elif num2>num1 and num3<num1:
		return num2
	elif num3>num1 and num1>num2:
		return num3
	elif num2>num1 and num1>num3:
		return num2
	elif num1>num3 and num3>num2:
		return num1
	else:
		return num1
print(max_de_tres(2,4,6))

print("ejercicio 3")


#3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.



def contar_caracteres(a_contar):
	contador=0
	for i in a_contar:
		contador=contador+1
	return contador

lista=["hola", 2.3, False]

frase="Hola mundo"
print(contar_caracteres(frase))

print("ejercicio 4")
#4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal(caracter):
	if caracter=="A" or caracter=="a" or caracter=="E" or caracter=="e" or caracter=="I" or caracter=="i" or caracter=="O" or caracter=="o" or caracter=="U" or caracter=="u":
		return True
	else:
		return False

print(es_vocal("a"))

print("ejercicio 5")

#5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sumar(lista):
	'''contador=0
	for i in lista:

		i=i+contador
		contador=i
	return i'''
	contador=0
	for i in lista:
		contador=contador+i
	return contador

def multiplicar(lista):
	
	contador=1
	for i in lista:
		contador=contador*i
	return contador

lista=[1,2,3,8]
print(sumar(lista))
print(multiplicar(lista))

print("ejercicio 6")

#6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(al_reves):
	for i in range(len(al_reves)-1,-1,-1):
		print(al_reves[i], end=" ")

inversa("juanjo")

print("")

print("ejercicio 7")

#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
	aux=""
	for i in range(len(palabra)-1,-1,-1):
		aux=aux+palabra[i]

	if palabra==aux:
		return True
	else:
		return False

print(es_palindromo("radar"))

#8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. 

print("")

print("ejercicio 9")

#9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_caracteres(factor_multiplicador,caracter):
	for i in range(factor_multiplicador):
		print(caracter, end=" ")

generar_caracteres(15,"*")
print("")

print("ejercicio 10")

'''10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******           '''




