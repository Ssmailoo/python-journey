# kalkulator BMI sederhana
'''def hitung_bmi(berat_kg, tinggi_m):
    bmi = berat_kg / (tinggi_m ** 2)
    return round(bmi, 2) 

berat = float(input("Berat (kg): "))
tinggi = float(input("Tinggi (m): "))

hasil hitung_bmi(berat, tinggi)
print(f"BMI anda: {hasil}")

if hasil < 18.5:
    print("Kategori : underweight")
elif hasil < 25:
    print("Kategori : normal")
elif hasil < 30:
    print("Kategori : Overweight")
else:
    print("Kategori : Obese") '''

import csv
import os

def expanse():
    while True:
        print("\n=== Expanse Tracker ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total per Kategori")
        print("4. Keluar")
        print("5. Bantuan")

        hasil = int(input("Pilih menu: "))

        if hasil == 1:
            tambah_pengeluaran()

        elif hasil == 2:
            lihat_pengeluaran()

        elif hasil == 3:
            total_per_kategori()

        elif hasil == 4:
            print("Keluar dari Program")
            break

        elif hasil == 5:
            print("Panduan penggunaan Expanse Tracker")

        else:
            print("Pilihan tidak valid")

pengeluaran = []

def tambah_pengeluaran():
    nama = input("masukkan nama: ")
    jumlah = int(input("masukkan jumlah: "))
    kategori = input("masukkan kategori: ")

    data = {
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori
    }

    pengeluaran.append(data)
    simpan_ke_csv()

def lihat_pengeluaran():
    if not pengeluaran:
        print("beluam ada pengeluaran")

    else:
        for i in pengeluaran:
            print(f"Nama: {i['nama']}, Jumlah: {i['jumlah']}, Kategori: {i['kategori']}")

def total_per_kategori():
    total = {}
    for item in pengeluaran:
        kategori = item["kategori"]
        jumlah = item["jumlah"]

        if kategori in total:
            total[kategori] = total[kategori] + jumlah

        else:
            total[kategori] = jumlah
    for kategori, jumlah in total.items():
        print(f"Kategori: {kategori}, Jumlah: {jumlah}")
def simpan_ke_csv():
    with open("expanse tracker.csv", mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=["nama", "jumlah", "kategori"])
        writer.writeheader()
        writer.writerows(pengeluaran)
def muat_dari_csv():
    if os.path.exists("expanse tracker.csv"):
        with open("expanse tracker.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for baris in reader:
                pengeluaran.append(baris)
muat_dari_csv()
expanse()