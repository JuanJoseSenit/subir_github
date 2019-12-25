

tabla_multiplicar=6

#CON CICLO FOR

for i in range(11):
	print(str(tabla_multiplicar) + "x" + str(i) + "=" + str(i*tabla_multiplicar))

print(" ")

#CON CICLO WHILE

i=0  #en el while hay que especificar el valor de i donde va a empezar
while i<=10:
	print(str(tabla_multiplicar) + "x" + str(i) + "=" + str(i*tabla_multiplicar))
	i=i+1

