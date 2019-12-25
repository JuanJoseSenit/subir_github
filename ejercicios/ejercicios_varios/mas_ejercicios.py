#http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-2.html

#http://www.pythondiario.com/p/ejercicios-de-programacion-python.html


'''Ejercicio 1
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.'''

print("EJERCICIO 1")
def max_in_list(lista):
	return max(lista)

lista=[2,320,87]
print(max_in_list(lista))

'''Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.'''
print("EJERCICIO 2")

def mas_larga(lista_palabras):
	long=0
	for i in lista_palabras:
		if len(i)>long:
			long=len(i)
			palabra=i
		else:
			continue
	print(palabra)
		
lista_palabras=["Tren", "Avioneta","Ave"]
mas_larga(lista_palabras)

'''Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.'''
print("EJERCICIO 3")

def filtrar_palabras(conjunto_palabras,n):
	for i in conjunto_palabras:
		if len(i)>n:
			print(i)
		else:
			continue 
conjunto_palabras=["Tren", "Avioneta","Ave"]
filtrar_palabras(conjunto_palabras,3)

'''Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir
 cuantas letras mayúsculas tiene. '''
print("EJERCICIO 4")

frase=input("Ingrese una frase por favor: ")
contador=0

for i in frase:
	if i.isupper()==True:
		contador=contador+1
	else:
		continue

print("El número de mayúsculas que tiene la palabra/frase que ha introducido es de: " + str(contador))


print("EJERCICIO 5")

'''Construir un pequeño programa que convierta números binarios en enteros. '''

#de binario a decimal
numero_binario=str(100)
numero_binario=numero_binario[::-1]  #invierte un numero
numero=0

for i in range(len(numero_binario)-1,-1,-1):

	if numero_binario[i]=="0":
		continue
	else:
		numero=numero+(pow(2,i))

print(numero)

#de decimal a binario
numero_decimal=466
matriz=[]

while numero_decimal/2!=0:
	numero=numero_decimal%2
	numero_decimal=int(numero_decimal/2)
	matriz.append(numero)
matriz=matriz[::-1]
print(matriz)

print("EJERCICIO 6")

'''Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.'''

ano_en_curso=str(input("Introduce el año en curso: "))

ano_en_curso=int(ano_en_curso)

nombre1=input("Introduzca el nombre de la persona 1: ")
ano_nacimiento1=str(input("Ingrese año de nacimiento de la persona 1: "))
ano_nacimiento1=int(ano_nacimiento1)

nombre2=input("Introduzca el nombre de la persona 2: ")
ano_nacimiento2=str(input("Ingrese año de nacimiento de la persona 2: "))
ano_nacimiento2=int(ano_nacimiento2)

nombre3=input("Introduzca el nombre de la persona 3: ")
ano_nacimiento3=str(input("Ingrese año de nacimiento de la persona 3: "))
ano_nacimiento3=int(ano_nacimiento3)

resultado={nombre1:((ano_en_curso)-(ano_nacimiento1)),nombre2:((ano_en_curso)-(ano_nacimiento2)),nombre3:((ano_en_curso)-(ano_nacimiento3))}
print("En el año "+ str(ano_en_curso) + " la edad de los ususarios será:" + "\n " + str(resultado))

print("EJERCICIO 7")
'''Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.'''

matriz_edades=[]
contador=0

for i in range(10):
	edad=int(input("Introduzca edad numero "+ str(i+1) + ": "))
	matriz_edades.append(edad)
	if matriz_edades[i]>20:
		contador=contador+1
	else:
		continue
tupla_edades=tuple(matriz_edades)


print("La tupla de edades introducidas es: " + str(tupla_edades))
print("El número de edades superiores a 20 años es de: " + str(contador))

print("EJERCICIO 8")
'''Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)'''

longitud_matriz=int(input("¿Cuántos nombres tiene la lista?: "))
nombres_matriz=[]

for i in range(longitud_matriz):
	nombre=input(" Introduzca el nombre del usuario " + str(i+1) + ": ")
	nombre=nombre.upper()
	nombres_matriz.append(nombre)

letra_inicial=input("Escriba la letra inicial del/los nombres a los que quiere acceder: ")
letra_inicial=letra_inicial.upper()

for i in nombres_matriz:
	if i[0]==letra_inicial:
		print(i)
	else:
		continue


print("EJERCICIO 9")
'''Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.'''

def contar_vocales(palabra,contador):
	palabra=palabra.upper()

	for i in palabra:
		
		if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
			contador=contador+1
		else:
			continue
	print("El numero total de vocales es de " + str(contador))


	contadorA=0
	contadorE=0
	contadorI=0
	contadorO=0
	contadorU=0
	for i in palabra:
		if i=="A":
			contadorA=contadorA+1
		elif i=="E":
			contadorE=contadorE+1
		elif i=="I":
			contadorI=contadorI+1
		elif i=="O":
			contadorO=contadorO+1
		elif i=="U":
			contadorU=contadorU+1
		else:
			continue
	print("El numero de A es de " + str(contadorA))
	print("El numero de E es de " + str(contadorE))
	print("El numero de I es de " + str(contadorI))
	print("El numero de O es de " + str(contadorO))
	print("El numero de U es de " + str(contadorU))




contador=0   #este es el contador de todas las vocales. si no le meto dentro de la funcion, se lo tengo que pasar por argumento
palabra=input("Introduzca la palabra que quiere analizar: ")

contar_vocales(palabra,contador)

print("EJERCICIO 10")


'''Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400'''


def es_bisiesto(anno):

	if anno%400==0:
		print("Es bisiesto")
	elif anno%100==0:
		print ("No bisiesto")
	elif anno%4==0:
		print("Es bisiesto")
	else:
		print("No es bisiesto")


anno=int(input("Introduzca un año: "))

es_bisiesto(anno)


