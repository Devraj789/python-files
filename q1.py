import random

i=0
counter = 0
counters = 0
countersa = 0

if(i<10):
	d = random.randint(1,100)
	e = random.randint(1,100)
	f = random.randint(1,100)
	counter = counter + d
	counters = counters + e
	countersa = countersa + f
	i=i+1
    	
	
	
print('Sum of 1st counter is:',counter)
print('Sum of 2nd counter is:',counters)
print('Sum of 3rd counter is:',countersa)

if(counter>counters and counter>countersa):
	print('gift is taken by counter1')
elif(counters>counter and counters>countersa):
	print('Gift is taken by counter 2')
else:
	print('Gift is taken by counter 3')

    
   

