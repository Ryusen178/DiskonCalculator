import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Panggil pdb di sini jika ingin melakukan debug log
        # pdb.set_trace() 

        # Perbaikan Bug: Persentase harus dibagi 100
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        # Perhitungan harga akhir yang benar
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir