# tulis solusi code disini

class Barang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_biaya(self):
        volume = self.hitung_volume()
        biaya_volume = 0
        if volume > 50:
            biaya_volume = (volume - 50) * 200

        biaya_berat = self.berat * 5000
        total_biaya = biaya_volume + biaya_berat
        return total_biaya

barang = Barang(5, 2, 4, 1)
biaya_ongkir = barang.hitung_biaya()

print(f"Harga Ongkir: Rp {biaya_ongkir}")