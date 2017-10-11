import random
a = random.randint(1,10)
b = int(input('Enter the number'))

if(b == a):
	print('You guessed it perfectly')
elif(b > a):
	print('You entered the higher value than CPU predicted value')
else:
	print('You entered the lower value than CPU predicted value')