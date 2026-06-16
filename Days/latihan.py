'''nama = "ismail"
umur = 26
tinggi = 1.75
aktif = True

print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(aktif))

print(f"Nama saya {nama}, umur {umur} tahun, tinggi {tinggi} cm, aktif {aktif}")
# f" adalah menyisipkan nilai variable langsung ke dalam teks
umur = 26

if umur >= 18:
    print("Dewasa")

elif umur >= 13:
    print("Remaja")

else:
    print("Anak-anak")

# belajar if else
def nilai():
    
    nilai = int(input("Masukkan Nilai"))

    if nilai < 0 or nilai > 100: # edge case
        print("Nilai tidak valid")
    
    elif nilai >= 90:
        print("Lulus dengan pujian")

    elif nilai >= 70:
        print("Lulus")

    else:
        print("Remedial")

nilai()


# program yang mencetak semua angka genap dari 1 sampai 20 (for loop)
for i in range (1, 21):
    if i % 2 == 0: # jika sisa bagi 2 adalah 0, berarti genap
        print(i)

# belajar mencetak angka 1 sampai 100 (while loop)
def program():
    nilai = 0
    for angka in range (1, 101):
        nilai = nilai + angka
    print(nilai)
    
program()

#list dan dictionary
friends = [
    {"nama": "agas", "kota": "topogaro"},
    {"nama": "iccang", "kota": "makassar"},
    {"nama": "mulky", "kota": "baringin"},
]

for item in friends:
    print(f"{item['nama']}: kota {item['kota']}")
print(f"Total teman: {len(friends)}")

def hitung_luas(p, l):
    return(p * l)

def kategori_umur(umur):
    if umur < 13:
        return "Anak-anak"
    elif umur <= 17:
        return "Remaja"
    else:
        return "Dewasa"
    
umur = int(input("Masukkan Umur"))
hasil = kategori_umur(umur)
print(hasil)



def total_belanja(belanja):
    total = 0
    for item in belanja:
        total = total + item
    return total

pengeluaran = [20000, 25000, 35000]
print(total_belanja(pengeluaran))'''

#=========== EXPANSE TRACKER ===========

'''def tambah_pengeluaran 

    pengeluaran = [
        input({"nama": "Kopi", "jumlah": 25000, "kategori": "Makanan"})
]'''
pengeluaran = []

def tambah_pengeluaran():
    nama = input("Nama item: ")
    jumlah = int(input("Jumlah: "))
    kategori = input("Kategori: ")
    item = {"nama": nama, "jumlah": jumlah, "kategori": kategori}
    pengeluaran.append(item)
    print("Pengeluaran berhasil ditambahkan.")

def lihat_pengeluaran():
    if len(pengeluaran) == 0:
        print("Belum ada pengeluaran")
    else:
        for item in pengeluaran:
            print(f"{item['nama']} - Rp{item['jumlah']} ({item['kategori']})")

tambah_pengeluaran()
tambah_pengeluaran()
lihat_pengeluaran()

def total_per_kategori():
    total = {}
    for item in pengeluaran:
        if item ['kategori'] in total:
            total[item['kategori']] = total[item['kategori']] + item['jumlah']
        else:
            total[item['kategori']] = item['jumlah']
    for kategori, jumlah in total.items():
        print(f"{kategori}: Rp{jumlah}")

total_per_kategori()

def menu():
    while True:
        print("1. tambah_pengeluaran")
        print("2. lihat_pengeluaran")
        print("3. total_per_kategori")
        print("4. break")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            tambah_pengeluaran()
        elif pilihan == 2:
            lihat_pengeluaran()
        elif pilihan == 3:
            total_per_kategori()
        else:
            break

    menu()
        



