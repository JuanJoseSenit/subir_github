'''Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota 
y si ha aprobado o no'''


class alumno():
	def inicializar_atributos(self,nombre,apellido,nota):
		self.nombre=nombre
		self.apellido=apellido
		self.nota=nota
	def imprimir_datos(self):
		print("Nombre: " + self.nombre)
		print("Apellido: " + self.apellido)
		print("Nota: " + str(self.nota))
	def aprobar(self):
		if self.nota>=5:
			print("Aprobado")
		else:
			print("Suspenso")


alumno1=alumno()
alumno1.inicializar_atributos("Juanjo","Senit",8)
alumno1.imprimir_datos()
alumno1.aprobar()

alumno2=alumno()
alumno2.inicializar_atributos("Javi", "Senit",4)
alumno2.imprimir_datos()
alumno2.aprobar()




