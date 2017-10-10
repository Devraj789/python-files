f = open("a.py","r")
# line = f.read(3)
# print line
# lines = f.read()
# print lines
# l = f.read()
# print l
# f.close()

d = []
b = f.read()
c = b.split(" ")
d['Name'] = c[0]
d['age'] = c[3]
d['occupation']= c[5]
print(d)
f.close()