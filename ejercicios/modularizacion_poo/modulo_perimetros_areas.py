import math

class cuadrado():
	def __init__(self,lado):
		self.lado=lado
	def calcular_perimetro(self):
		return 4*self.lado
	def calcular_area(self):
		return (self.lado*self.lado)


class rectangulo():
	def __init__(self,base,altura):
		self.base=base
		self.altura=altura
	def calcular_perimetro(self):
		return (2*self.base+2*self.altura)
	def calcular_area(self):
		return (self.base*self.altura)

class circulo():
	def __init__(self,radio):
		self.radio=radio
	def calcular_perimetro(self):
		return (2*math.pi*self.radio)
	def calcular_area(self):
		return (math.pi*pow(self.radio,2))




