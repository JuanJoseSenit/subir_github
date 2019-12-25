from io import open

archivo=open("contador.txt","w")
archivo.write("0")

archivo.close()

while True:

	cadena=input("Inc o Dec: ")
	cadena=cadena.upper()



	if cadena=="INC":
		archivo=open("contador.txt","r")
		valor=archivo.read()
		valor=int(valor)
		valor=valor+1
		valor=str(valor)
		archivo.close()
		archivo=open("contador.txt","w")  #cuando abres el modo escritura, se borra lo que habia en el txt. nos viene bien porque solo queremos que nos muiestre el nuevo valor
		archivo.write(valor)
		archivo.close()

	elif cadena=="DEC":
		archivo=open("contador.txt","r")
		valor=archivo.read()
		valor=int(valor)
		valor=valor-1
		valor=str(valor)
		archivo.close()
		archivo=open("contador.txt","w")  #cuando abres el modo escritura, se borra lo que habia en el txt. nos viene bien porque solo queremos que nos muiestre el nuevo valor
		archivo.write(valor)
		archivo.close()




