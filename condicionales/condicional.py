print("introduzca la nota del primer examen")
nota1=int(input())    #para python lo que se entroduce por consola es siempre un string. si queremos introducir un numero poner int()

print("introduzca la nota de su segundo examen")
nota2=int(input())


notamedia=(nota1+nota2)/2

if notamedia<5:
	print ("suspenso")
if notamedia>=5:
	print("aprobado")
	