class Cancion():
	def __init__(self,titulo="",autor=""):
		self.__titulo=titulo
		self.__autor=autor
	def get_titulo(self):
		return self.__titulo
	def set_titulo(self,titulo):
		self.__titulo=titulo


	def get_autor(self):
		return self.__autor
	def set_autor(self,autor):
		self.__autor=autor

	def imprimir(self):
		return "El título de la canción es: " + self.__titulo + " y su autor es : " + self.__autor
	def invertir(self):
		nuevo_titulo=self.__autor
		nuevo_autor=self.__titulo
		self.__autor=nuevo_autor
		self.__titulo=nuevo_titulo


cancion1=Cancion("Un mundo ideal","Aladin")
#print(cancion1.__titulo)         Al ser privado, no puedo acceder a sus atributos desde fuera directamente
print(cancion1.get_titulo())
print(cancion1.get_autor())

cancion1.set_titulo("Un genio tan genial")
print(cancion1.get_titulo())

print(cancion1.imprimir())
cancion1.invertir()
print(cancion1.imprimir())

nuevo_titulo=cancion1.get_autor()
nuevo_autor=cancion1.get_titulo()
cancion1.set_titulo(nuevo_titulo)
cancion1.set_autor(nuevo_autor)
print(cancion1.imprimir())



