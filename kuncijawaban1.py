# Soal 1
# nama = input("Nama Anda: ")
# umur = int(input("Umur Anda: "))
# tinggi = float(input("Tinggi Badan Anda: "))
# print("Nama saya {}, umur saya {} tahun dan tinggi saya {} cm.".format(nama,umur,tinggi))

# Soal 2
# jari = int(input("Masukkan Jari-jari lingkaran: "))
# r = 22/7*jari**2
# print(f"Luas lingkaran dengan jari-jari {jari} cm adalah {r:.2f} cm².")

# Soal 3
teori = int(input("Masukkan Nilai Teori: "))
praktek = int(input("Masukkan Nilai Praktek: "))
if teori >= 70 and praktek >= 70:
	print("Selamat, anda lulus!")
elif teori >= 70 and praktek < 70:
	print("Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70:
	print("Anda harus mengulang ujian teori.")
else:
	print("Anda harus mengulang ujian teori dan praktek.")
