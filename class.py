class KelasSaya:
	__author__ = "Fadzarar"
	def __init__(self,name,age):
		self.nama = name
		self.umur = age
	def sayHi(self):
		print("Hi!")
	def introduce(self):
		print(f"My name is {self.nama} and I'm {self.umur} years old")

print(dir(KelasSaya.__author__))