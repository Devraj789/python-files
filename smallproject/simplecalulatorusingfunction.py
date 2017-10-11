def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y


print('Choose the operation for processing')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')

choice = int(input('Enter the numbers from 1 to 4 for transaction'))
n1 = int(input('Enter the first number'))
n2 = int(input('Enter the second number'))

if(choice == 1):
	print('Addition is :',add(n1 ,n2))
elif(choice == 2):
	print('Subtraction is :',sub(n1,n2))
elif(choice == 3):
	print('Multiplication is :',mul(n1 ,n2))
elif(choice == 4):
	print('Division is :',div(n1,n2))
else:
	print('Invalid arguments')
	
