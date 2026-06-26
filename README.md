# Python Journey

Repositori ini berisi perjalanan belajar Python saya,
dari dasar hingga integrasi API publik.

# Expense Tracker by Ssmailoo
Expense tracker ini adalah projek yang saya buat untuk mencatat pengeluaran saya.

## Tech Stack
- Python 3.14
- csv, os (standard library)

## Fitur
- Tambah pengeluaran
- Lihat pengeluaran
- Total per kategori
- Keluar
- Bantuan

## Cara Menjalankan
1. Clone repository ini
   git clone https://github.com/Ssmailoo/python-journey.git

2. Masuk ke folder project
   cd python-journey/projects/expense-tracker

3. Buat virtual environment
   python3 -m venv venv

4. Aktifkan virtual environment
   source venv/bin/activate

5. Jalankan program
   python3 main.py

## Yang Dipelajari
- File I/O dan csv
- Error handling
- Fungsi dan SRP(Single Responsibility Principle), artinya satu fungsi untuk satu tugas

## Projects

### Weather + GitHub Dashboard

Program yang mengambil data cuaca Makassar secara realtime
dari OpenWeatherMap API dan data profil GitHub,
lalu menampilkan summary harian di terminal.

### Teknologi

- Python
- requests
- json

### Cara Menjalankan

1. Clone repository
   git clone https://github.com/Ssmailoo/python-journey.git

2. Masuk ke folder project
   cd python-journey

3. Buat dan aktifkan virtual environment
   python -m venv venv
   source venv/bin/activate

4. Install dependency
   pip install -r requirements.txt

5. Tambahkan API key OpenWeatherMap di file dashboard.py

6. Jalankan program
   cd api-practice
   python dashboard.py

### Yang Dipelajari

- Cara hit API publik dengan requests
- Parsing JSON dari response API
- Konversi data antara JSON dan Python
- Menyimpan data ke file JSON lokal
- Git branching workflow