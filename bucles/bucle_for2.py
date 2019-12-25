lista=["casa","mesa","avion"]

for i in lista:
	print(i)

for i in range(0,len(lista)):
	print(lista[i])


lista2=[10,8,15,14,1]
print(lista2)

listafinal=[]
for i in range(0,len(lista2)):
	if lista2[i]<=10:
		listafinal.append(lista2[i])
print(listafinal)

