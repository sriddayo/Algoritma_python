# Membuat list kosong untuk menyimpan nama barang
belanja = []

# Meminta pengguna memasukkan 5 nama barang
for i in range(5):
    barang = input("Masukkan nama barang ke-" + str(i + 1) + ": ")
    belanja.append(barang)

# Menampilkan total item dan 3 item pertama
print("\nTotal item:", len(belanja))
print("3 item pertama:", belanja[:3])