for i in range(5):   #i desde 0 a 4
	print(i, end="  ")
print(" ")


for i in range(5,10):   #i desde 5 hasta el 9
	print("i vale: " + str(i))


for i in range(5,10):   #i desde 5 hasta el 9
	print(f"valor de la variable {i}")  #de esta forma podemos unir un texto a una variable sin tener que concatenar

for i in range(5,50,3):  #desde el 5 al 49 de tres en tres
	print (i, end="-")