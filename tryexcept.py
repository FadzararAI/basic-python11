try:
	coba = int(input("Masukkan Angka: "))
except ValueError:
	print("Data tidak sesuai dengan kriteria!")
except KeyboardInterrupt:
	print("Program dihentikan!")
else:
	print(f"Anda Menginputkan angka {coba}")
finally:
	print("Program Selesai!")
