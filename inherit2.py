class Bank:
	def __init__(self,name,Accountno,balance):
		self.name = name
		self.Accountno = Accountno
		self.balance = balance

	def withdraw(self,a):
		if(a>self.balance):
			print("Not enough balance")
		else:
			self.balance = self.balance-a
			print("You withdraw is",a)
	def deposit(self ,a):
		self.balance = self.balance + a
		print('Rs',a,'Succesfully deposited')

	def getbalance(self):
		print("Your current balance is",self.balance)


class Customer(Bank):
	def __init__(self,name,address,phone,Accountno,balance):
		super().__init__(name,Accountno,balance)
		self.address = address
		self.phone = phone
	    

		
c1 = Customer("dev",'Dhading',18237891,34,317838)
c1.withdraw(500)
c1.getbalance()
c1.deposit(100000)
c1.getbalance()
