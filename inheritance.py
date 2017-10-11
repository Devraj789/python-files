class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __str__(self):
		return self.name + " " + str(self.age)

class Employee(person):
	def __init__(self,name,age,eid):
		super().__init__(name,age)
		self.eid = eid

	def __str__(self):
		return super().__str__()+ " " + self.eid

X = Employee('abc',20,'1234Xy')
print(X)