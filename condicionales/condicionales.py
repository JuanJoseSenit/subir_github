#IF

print("introduzca la nota del primer examen")
nota1=int(input())   #para python lo que se entroduce por consola es siempre un string. si queremos introducir un numero poner int()

print("introduzca la nota de su segundo examen")
nota2=int(input())

def media(nota1,nota2):
	notamedia=(nota1+nota2)/2
	return notamedia

if media(nota1,nota2)>=5:
	print("aprobado")
else:
	print("suspenso")