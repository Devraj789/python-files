
def fibonacci(n):
	a = 0
	b = 1
	i = 1
	print(a)
	print(b)
	while (i<=n):
		 c = a + b
		 a = b
		 b = c
		 print(c)
		 i = i + 1

d = int(input("Enter the value of n"))
fibonacci(d)
  
