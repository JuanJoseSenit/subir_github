'''Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.'''

#LO HICE SIN INTRODUCIR LOS VALORES POR TECLADO
class calculadora():
	def __init__(self,numero1,numero2):
		self.num1=numero1
		self.num2=numero2
	def sumar(self):
		self.suma=self.num1+self.num2
		print(str(self.num1) + "+" + str(self.num2) + "=" + str(self.suma))
	def restar(self):
		self.resta=self.num1-self.num2
		print(str(self.num1) + "-" + str(self.num2) + "=" + str(self.resta))
	def multiplicar(self):
		self.multiplicacion=self.num1*self.num2
		print(str(self.num1) + "x" + str(self.num2) + "=" + str(self.multiplicacion))
	def dividir(self):
		try:
			self.division=self.num1/self.num2
			print(str(self.num1) + "/" + str(self.num2) + "=" + str(self.division))
			
		except ZeroDivisionError:
			print("No se puede dividir entre 0")

	

op1=calculadora(15,0)
op1.sumar()
op1.restar()
op1.multiplicar()
op1.dividir()