nombre=input("Introduzca su nombre: ")
direccion=input("Intoduzca su dirección: ")
telefono=int(input("Introduzca su telefono: "))

mis_datos=[nombre,direccion,telefono]

diccionario={"Nombre":mis_datos[0],"Dirección":mis_datos[1],"Teléfono":mis_datos[2]}
print("Sus datos personales son: " + str(diccionario))
print(diccionario)