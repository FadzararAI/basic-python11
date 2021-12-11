# QUiz
n = int(input("How many persons: "))
person_name = []
for i in range(n):
	name = input("Person's Name: ")
	person_name.append(name)
print(" ")
print("All of the persons name")
for x in person_name:
	print(x)