class NIF():
	def __init__(self):
		self.__dni=input("Introduzca el número de su dni: ")
		self.__letra=self.calcular_letra()
	def get_dni(self):
		return self.__dni
	def get_letra_dni(self):
		return self.__letra

	def calcular_letra(self):
		letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X','B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
		longitud_matriz=len(letras)


		numero_dni=int(self.get_dni())
		numero_dividido=numero_dni%longitud_matriz
		letra=letras[numero_dividido]

		return letra
	def imprimir(self):
		return self.get_dni() + "-" + self.get_letra_dni()


'''dni1=NIF()
print(dni1.imprimir())'''

