# a = 10
# b = 10
# if a > b: # False
# 	print("Nilai dari A lebih besar dari B")
# elif b > a: # False
# 	print("Nilai dari A tidak lebih besar dari B")
# else: # True
#  	print("Nilai A dan B sama")
print("##### Login Page #####")
username = input("Input Username: ") # Admin
code = int(input("Input Password: ")) # 321

if username in "Lucky" and code == 123 or code == 321:
	print("Login Success!")
else:
	print("Login Failed!")