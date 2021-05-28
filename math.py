#Add function
def add(x, y):
	return x + y 
#Subtract function
def sub(x, y):
	return x - y
def mul(x, y):
	return x * y # on bug4566
def div(x, y):
	if y == 0:
		return "error" # on bug4566 
	else :
		return x / y
