# daftar_belanja = ["Keset", "Taplak meja", "Tudung", "Serbet"]
# # barang = "Serbet"
# for barang in daftar_belanja:
# 	print(barang)
#range(start,stop,step)
# for x in range(1,11,3):
# 	print(x)

# banyak_barang = int(input("Banyak barang yang dilist: ")) # 5
# barang = []

# for i in range(banyak_barang):
# 	nama_barang = input("Nama barang: ") # Meja
# 	barang.append(nama_barang)

# print(" ")

# print("Barang-barang yang ada di list: ")

# for x in barang:
# 	print(x)

# for i in range(1,10):
# 	if i == 5:
# 		print("ini ke-lima")
# 		break
# 	print(i)

# Nested Loop
# for i in range(5):
# 	print("Ini Loop luar")
# 	for x in range(3):
# 		print("Ini Loop dalam")
# Pyramid
# for i in range(5,-5,-1):
#       for j in range(i):
#             print(i,end='')
#       print()

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 3, 5, 6]
# z = 0

# for i in x :
# 	print(i)
# 	for j in y :
# 		print(j)
# 		if i == j :
# 			z =z+1

# print(z)

name = ["Ismail","Ali","Elif"]
number = [1,2,3]
cars = ["Mercedes","Porshe","Hyundai"]
for names in name:
	for num in number:
		for car in cars:
			print(f"{names} has {num} {car}")