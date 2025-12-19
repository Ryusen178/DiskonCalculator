# Laporan Debugging (DEBUG_REPORT.md)

**Masalah:** Munculnya bug PPN 10% yang menyebabkan harga akhir lebih tinggi dari harga setelah diskon yang seharusnya.

**Langkah Penelusuran menggunakan PDB:**
1. Mengaktifkan `pdb.set_trace()` di dalam metode `hitung_diskon`.
2. Menjalankan skrip dan menggunakan perintah `n` (next) untuk baris demi baris.
3. Menggunakan perintah `p harga_akhir` untuk memeriksa nilai sebelum return.

**Bukti Penelusuran (Output Command):**
- `(Pdb) p jumlah_diskon` -> 100.0 (Sesuai)
- `(Pdb) p harga_akhir` -> 900.0 (Sesuai sebelum PPN)
- `(Pdb) n` (Melewati baris bug PPN)
- `(Pdb) p harga_akhir` -> 990.0 (Terdeteksi bug: Nilai bertambah 10% secara tidak sengaja)

**Solusi:**
Menghapus baris kode `harga_akhir = harga_akhir + (harga_akhir * 0.1)` agar perhitungan kembali murni ke diskon.