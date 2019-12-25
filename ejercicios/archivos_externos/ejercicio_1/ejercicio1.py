from io import open
'''Escribir una función que pida un número entero entre 1 y 10 y 
guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar 
de ese número, done n es el número introducido.'''



def comprobar_numero(numero):
	while numero!=1 and numero!=2 and numero!=3 and numero!=4 and numero!=5 and numero!=6 and numero!=7 and numero!=8 and numero!=9 and numero!=10:
		numero=str(input("Recuerde que el número debe ser un entero entre 1 y 10: "))
		numero=float(numero)
	return numero

def calcular_tabla(numero):
	matriz=[]
	for i in range(11):
		valor=numero*i
		matriz.append(valor)
	
	archivo=open("tabla.txt", "w")
	archivo.write(str(matriz))
	archivo.close
	return matriz



numero=str(input("Introduce un número del 1 al 10: "))
numero=float(numero)
numero=comprobar_numero(numero)

print(calcular_tabla(numero))

#print(numero)