# Verifikasi Kode: Debugging dan Unit Testing Sederhana
### Praktikum Pemrograman Berorientasi Objek (PBO)

Proyek ini bertujuan untuk mendemonstrasikan proses verifikasi kode melalui teknik **Debugging** menggunakan `pdb` dan **Unit Testing** menggunakan framework `unittest` pada Python. Proyek ini mensimulasikan perbaikan bug pada sistem kalkulator diskon.

## 📂 Struktur File
* `diskon_service.py`: Logika utama perhitungan diskon dengan kelas `DiskonCalculator`.
* `test_diskon.py`: Unit test dasar untuk menguji fungsionalitas utama.
* `test_diskon_advanced.py`: Unit test lanjutan untuk menangani nilai *float* dan *edge cases*.
* `DEBUG_REPORT.md`: Laporan teknis proses debugging.

## 🛠️ Fitur & Skenario Pengujian
Program ini mencakup pengujian terhadap beberapa kondisi berikut:
1.  **Diskon Standar**: Memastikan diskon 10% dihitung dengan benar.
2.  **Boundary Condition**: 
    * Diskon 0% (harga tidak berubah).
    * Diskon 100% (harga menjadi nol).
3.  **Input Negatif**: Penanganan jika input diskon di bawah nol.
4.  **Floating Point**: Pengujian presisi desimal (diskon 33% pada harga 999) menggunakan `assertAlmostEqual`.
5.  **Edge Case**: Penanganan jika harga awal adalah 0.

## 🚀 Cara Menjalankan
### 1. Debugging
Untuk menjalankan sesi debugging secara interaktif menggunakan `pdb`, pastikan `pdb.set_trace()` aktif di file `diskon_service.py`, lalu jalankan:
```bash
python diskon_service.py
```
### 2. Unit testing
Jalankan perintah berikut di terminal untuk memverifikasi bahwa semua kode berfungsi dengan benar:
`python -m unittest test_diskon.py`, Menjalankan Test Dasar:
```bash
