'''Realizar un programa que tenga una clase Persona con las siguientes características. 
La clase tendrá como atributos el nombre y la edad de una persona. 
Implementar los métodos necesarios para inicializar los atributos, 
mostrar los datos e indicar si la persona es mayor de edad o no.'''

class persona():
	def __init__(self,nombre,edad):
		self.__nombre=nombre     #nombre está en privado por lo que persona1.__nombre no se puede usar desde fuera.Hay que crear un metodo para acceder a los atributos privados
		self.edad=edad
	def imprimir_datos(self):
		print("Nombre: " + self.__nombre)
		print("Edad: " + str(self.edad))
	def imprimir_mayoria(self):
		if self.edad<18:
			print("Menor de edad en España")
		elif self.edad>=18:
			print("Mayor de edad en España")
	def get_nombre(self):
		print(self.__nombre)
	def set_nombre(self,nombre):
		self.__nombre=nombre
		




persona1=persona("Juanjo",29)
#persona1.__nombre="Javi"
persona1.imprimir_datos()
persona1.imprimir_mayoria()
persona1.get_nombre()
persona1.set_nombre("Javi")
persona1.get_nombre()

