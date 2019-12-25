'''Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase 
con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño 
mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).'''



class triangulo():
	def __init__(self):
		self.lado1=int(input("Introduzca el valor del lado 1: "))
		self.lado2=int(input("Introduzca el valor del lado 2: "))
		self.lado3=int(input("Introduzca el valor del lado 3: "))

	def imprimir_lado_mayor(self):
		if self.lado1>self.lado2 and self.lado2>self.lado3:
			print("El lado mayor es lado 1: " + str(self.lado1))
		elif self.lado1>self.lado3 and self.lado3>self.lado2:
			print("El lado mayor es lado 1: " + str(self.lado1))
		elif self.lado2>self.lado1 and self.lado1>self.lado3:
			print("El lado mayor es lado 2: " + str(self.lado2))
		elif self.lado2>self.lado3 and self.lado3>self.lado1:
			print("El lado mayor es lado 2: " + str(self.lado2))
		elif self.lado3>self.lado1 and self.lado1>self.lado2:
			print("El lado mayor es lado 3: " + str(self.lado3))
		elif self.lado3>self.lado2 and self.lado2>self.lado1:
			print("El lado mayor es lado 3: " + str(self.lado3))

	def tipo_triangulo(self):
		if self.lado1==self.lado2 and self.lado2==self.lado3:
			print("El triángulo es equilátero")
		elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
			print("El triángulo es escaleno")
		else:
			print("El triángulo es isósceles")


triangulo1=triangulo()
triangulo1.imprimir_lado_mayor()
triangulo1.tipo_triangulo()
