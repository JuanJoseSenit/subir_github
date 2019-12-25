from io import open
'''Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número
, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''



def comprobar_numero(numero):
	while numero!=1 and numero!=2 and numero!=3 and numero!=4 and numero!=5 and numero!=6 and numero!=7 and numero!=8 and numero!=9 and numero!=10:
		numero=float(input("Recuerde que el número debe ser un entero entre 1 y 10: "))
		
	return numero
	'''while isinstance(numero,int)==False and nu:
		numero=str(input("Recuerde que el número debe ser un entero entre 1 y 10: "))
		numero=float(numero)
	return numero'''

def calcular_tabla(numero):
	matriz=[]
	for i in range(11):
		valor=numero*i
		matriz.append(valor)
	
	archivo=open("tabla.txt", "w")
	archivo.write(str(matriz))
	archivo.close
	

numero=float(input("Introduce un número del 1 al 10: "))

numero=comprobar_numero(numero)
calcular_tabla(int(numero))

archivo=open("tabla.txt", "r")
lectura_pdf=archivo.read()
archivo.close()
print(lectura_pdf)







