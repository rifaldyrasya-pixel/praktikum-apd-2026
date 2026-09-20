# 1. Daftar harga komponen roket
komponen_1 = 120000 
komponen_2 = 135000 
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

# Poin Plus: Memasukkan semua komponen ke dalam list harga_komponen
harga_komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]

# Biaya administrasi nota premium
biaya_admin = 15000

# 2. Hitung total biaya secara manual (tanpa fungsi sum())
total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_admin

# 3. Hitung rata-rata harga (total biaya dibagi jumlah data menggunakan len)
rata_rata = total_biaya / len(harga_komponen)

# 4. Variabel NIM (silakan ganti "22" dengan 2 digit terakhir NIM kamu)
nim = 73

# 5. Variabel boolean mengecek apakah NIM tidak sama dengan rata-rata
bolean = nim != rata_rata

# Poin Plus: Konversi total biaya ke Poundsterling (GBP)
# Kurs perkiraan: 1 GBP = Rp20.500
kurs_gbp = 20500
total_biaya_gbp = total_biaya / kurs_gbp

# 6. Menampilkan semua variabel ke layar
print("--- RINCIAN BIAYA PEMBELIAN KOMPONEN ---")
print("Daftar Harga Komponen :", harga_komponen)    
print("Total Biaya (Rp)      :", total_biaya)
print("Rata-rata Biaya       :", rata_rata)
print("NIM (2 digit terakhir):", nim)
print("Apakah NIM != Rata2   :", bolean)
print("Total Biaya (GBP)     : £", round(total_biaya_gbp, 2))

# Poin Plus: Menampilkan komponen 1 sampai 4 menggunakan slice index negatif
# Index negatif -6 adalah komponen_1 dan -2 adalah batas akhir (komponen_5, tidak terikut)
print("Komponen 1 sampai 4 (Slice Negatif):", harga_komponen[-6:-2])