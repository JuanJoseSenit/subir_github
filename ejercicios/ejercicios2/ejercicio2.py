

#FORMA CLASICA

contras="juanjo jkhnjknbhk"
contad=0
for i in range(len(contras)):
	if contras[i]==" ":
		contad=1
	

if contad>0 or len(contras)<8:
	print("Contraseña erronea")
else:
	print(("Contraseña OK"))



#FORMA EN PYTHON

entrada="juanjojkhijhijhjki hjbjguhyguyh"
if " " in entrada or len(entrada)<8:
	print("Contraseña erronea")
else:
	print("contraseña OK")
