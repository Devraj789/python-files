number=int(input("Enter a Number between 1 to 10\n"))
import random

n=random.randint(1,10)
print(n)
if(number==n):
	print("You Won")
else:
	print("Try again")