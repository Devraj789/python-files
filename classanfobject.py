class car:
	def __init__(self,wheelno):
	    self.wheelno = wheelno

	def getwheelno(self):
		return self.wheelno

c = car(4)
print(c.getwheelno())