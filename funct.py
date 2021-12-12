nama = []
def datanama(inputan):
	def simpandata():
		for i in range(banyak_data):
			nama_orang = input("Nama Orang: ")
			nama.append(nama_orang)
	def hapusdata():
		for posisi in range(len(nama)):
			print(posisi,nama[posisi])
		hapus = int(input("Data Yang Ingin Dihapus (Urutan): "))
		nama.pop(hapus)
	if inputan == 1:
		banyak_data = int(input("Banyak Data Yang Di-input: "))
		simpandata()
	elif inputan == 2:
		hapusdata()
	else:
		return
def tampilnama():
	print("(X) Semua Data Nama: ")
	for i in nama:
		print(i)
while True:
	print("############################")
	print("# Penyimpan Data Nama      #")
	print("############################")
	print("# 1. Mengatur Data Nama    #")
	print("# 2. Menampilkan Data Nama #")
	print("############################")
	print()
	pilihan = int(input("Masukkan Pilihan: "))
	print()
	if pilihan == 1:
		print("Pilihan:\n1. Simpan Data\n2. Hapus Data")
		inputan = int(input("Masukkan Pilihan: "))
		datanama(inputan)
		print()
	elif pilihan == 2:
		tampilnama()
		print()
	else:
		print("Opsi Tidak Ditemukan!")
