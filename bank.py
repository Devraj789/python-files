class Bank():
	def __init__(self,accountno,balance):
		self.accountno = accountno
		self.balance = balance
	def withdrawamount(self , a):
		if(a > self.balance):
			print('Not enough balance')
		else:
			print('amount has been withdrawed',a)
	def deposit(self , a):
		self.balance = self.balance + a
		print("You deposit :",a)
	def getbalance(self):
		print("Your current balance is:",self.balance)

class Person(Bank):
	def __init__(self,name,address,phone,accountno,balance):
		super().__init__(accountno,balance)
		self.name = name
		self.address = address
		self.phone = phone
		

c1 = Person("dev","Chhauni","9860157760",98,12	)
c1.getbalance()
c1.withdrawamount(100)
c1.getbalance()
c1.deposit(2000)
c1.getbalance()
