import random
def roll():
	n = random.randint(1,6)
	print(n)
n1 = random.randint(1,6)
print(n1)

i = 1
while(i>0):
	r2 = input("Do u wnt to roll again(y/n)")
	if(r2 == 'y'):
		roll()
	elif(r2 == 'n'):
		break
	else:
		print('Invalid arguments')
  