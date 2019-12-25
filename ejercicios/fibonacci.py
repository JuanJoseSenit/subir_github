#SERIE FIBONACCI

n1=0
n2=1

print(n1)
print(n2)


def Fibonacci(n1,n2):
	for i in range(5):
		n2=n2+n1
		n1=n2-n1
		print(n2)


Fibonacci(n1,n2)