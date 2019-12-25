import ejercicio_dni

class Persona():
	def __init__(self,nombre,direccion,codigopostal,ciudad,dni):
		self.__nombre=nombre
		self.__direccion=direccion
		self.__codigopostal=codigopostal
		self.__ciudad=ciudad
		self.__dni=dni  #ejercicio_dni.NIF()

	def imprimir(self):
		return "Nombre: " + self.__nombre + " Dirección: " + self.__direccion + " CP: " + str(self.__codigopostal) + " Ciudad: " + self.__ciudad + " DNI " + self.__dni.imprimir()


dni1=ejercicio_dni.NIF()
persona1=Persona("juanjo","Gran Via", 28030, "Madrid", dni1)
print(persona1.imprimir())