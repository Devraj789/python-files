class person:
	def __init__(self,name,phone,age):
		self.name = name
		self.phone = phone
		self.age =age
	def __str__(self):
		return self.name+" "+self.phone+" "+str(self.age)

x = person('dev','1234',25)
print(x)