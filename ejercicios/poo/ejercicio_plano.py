from math import *

#clase puntos

class punto():
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def string(self):
		punto="(" + str(self.x) + "," + str(self.y) + ")"
		return punto
	def cuadrante(self):
		if self.x>0 and self.y>0:
			return "primer cuadrante"
		elif self.x>0 and self.y<0:
			return "cuarto cuadrante"
		elif self.x<0 and self.y<0:
			return "tercer cuadrante"
		elif self.x<0 and self.y>0:
			return "segundo cuadrante"	
		else:
			return "origen de coordenadas"
	def vector(self,punto):
		x1=self.x
		y1=self.y
		x2=punto.x
		y2=punto.y
		x_vector=x2-x1
		y_vector=y2-y1
		return "El vector es (" + str(x_vector) + "," + str(y_vector) + ")"
	def distancia(self,punto):
		x1=self.x
		y1=self.y
		x2=punto.x
		y2=punto.y
		parentesis1=(x2-x1)**2
		parentesis2=(y2-y1)**2
		suma=parentesis1+parentesis2
		distancia=sqrt(suma)
		return distancia
class rectangulo():
	def __init__(self,punto1=punto(),punto2=punto()):
		self.punto1=punto1
		self.punto2=punto2
	def string(self):
		punto="(" + str(self.punto1.string()) + "," + str(self.punto2.string()) + ")"
		return punto
	def base(self):
		x1=self.punto1.x
		x2=self.punto2.x
		base=abs(x2-x1)
		return base
	def altura(self):
		y1=self.punto1.y
		y2=self.punto2.y
		altura=abs(y2-y1)
		return altura
	def area(self):
		area=self.base()*self.altura()
		return area



mipunto=punto(1,5)
mipunto2=punto(2,8)


'''print(mipunto.string())
print(mipunto.cuadrante())

print(mipunto2.string())
print(mipunto2.cuadrante())


print(mipunto.vector(mipunto2))
print(mipunto2.vector(mipunto))

print ("La distancia entre los dos puntos es de: " + str(mipunto.distancia(mipunto2)))

mirectangulo=rectangulo(mipunto,mipunto2)
print(mirectangulo.string())'''

mirectangulo=rectangulo(mipunto, mipunto2)

print(mirectangulo.base())
print(mirectangulo.altura())
print(mirectangulo.area())






