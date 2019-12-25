'''En este ejercicio deberás crear un script llamado personas.py que lea los datos de un fichero de texto,
que transforme cada fila en un diccionario y lo añada a una lista llamada personas. 
Luego rocorre las personas de la lista y paracada una muestra de forma amigable todos sus campos.'''

from io import open

archivo=open("personas.txt","r")

lectura=archivo.readlines()

print(lectura)


persona=[]
for i in range(0,len(lectura)):
	separador=";"
	campos_separados=lectura[i].split(separador)
	diccionario={"id":campos_separados[0],"nombre":campos_separados[1],"apellido":campos_separados[2],"nacimiento":campos_separados[3]}
	persona.append(diccionario)

print((persona[0])["apellido"])


	




