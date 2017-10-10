# calculator using function

def add(x,y):
	print(x+y)

def sub(x,y):
	print(x-y)

def mul(x,y):
	print(x*y)

def div(x,y):
	print(x/y)

print("Select operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

a = int(input("Enter the number between 1 to 4 for operation"))
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if(a == 1):
	print(add(num1 ,num2))
elif(a == 2):
	print(sub(num1 , num2))
elif(a == 3):
	print(mul(num1 ,num2))
elif(a == 4):
	print(div(num1 , num2))
else:
    print("sssWrong parameters")

