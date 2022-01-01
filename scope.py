x = 100
def coba():
	global x
	x = 200
coba()
print(x)
def coba2():
	global x
	x = 250
	print(x)
coba2()
print(x)