class aclass:
	fees  = 50000
	def __init__(self,name,address,score,major_subject):
		self.name = name
		self.address = address
		self.score = score
		self.major_subject = major_subject
		f = open("abc.py","w")
		tabledata = self.name ,self.address ,self.score ,self.major_subject,self.fees
		tabledatastr = str(tabledata)
		f.write(tabledatastr)
		f.write('\n')
		f.close()


    
	def discount(self):
		if(self.score>=50 and self.score<=60):
			return(self.fees-(self.fees*15)/100)
		elif(self.score>60 and self.score<=70):
			return(self.fees-(self.fees*20)/100)
		else:
			return(self.fees-(self.fees*30)/100)

f = open("abc.py","w")
tablehead = ("Name\tAddress\tScore\tfees\tTotalfees\n")
f.write(tablehead)
f.close()
dev = aclass("Dev","Chhauni",30,100)


