# tulis solusi code disini

class BangunDatar:
    def __init__(self) :
        self.sisi = None
        self.panjang = None
        self.lebar = None

    def hitung_luas(self) :
        pass

    def hitung_keliling(self) :
        pass

class Persegi(BangunDatar) :
    def __init__(self, sisi) :
        super().__init__()
        self.sisi = sisi

    def hitung_luas(self) :
        return self.sisi * self.sisi

    def hitung_keliling(self) :
        return 4 * self.sisi

class Segitiga(BangunDatar) :
    def __init__(self, alas, tinggi) :
        super().__init__()
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self) :
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self) :
        keliling = self.alas + self.tinggi
        sisi_miring = pow(self.alas**2 + self.tinggi**2, 0.5)
        keliling += sisi_miring
        return keliling

class PersegiPanjang(BangunDatar) :
    def __init__(self, panjang, lebar) :
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self) :
        return self.panjang * self.lebar

    def hitung_keliling(self) :
        return 2 * (self.panjang + self.lebar)

def hasil() :
    while True :
        bangun_datar = input("Pilih bangun datar (persegi, segitiga, persegi panjang): ").lower()
        if bangun_datar in ["persegi", "segitiga", "persegi panjang"] :
            break
        else :
            print("Input tidak valid. Masukkan salah satu dari: persegi, segitiga, persegi panjang.")

    if bangun_datar == "persegi" :
        sisi = float(input("Masukkan sisi: "))
        bangun = Persegi(sisi)

    elif bangun_datar == "segitiga" :
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        bangun = Segitiga(alas, tinggi)

    else :
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        bangun = PersegiPanjang(panjang, lebar)

    print(f"\nLuas {bangun_datar} : {bangun.hitung_luas()}")
    print(f"Keliling {bangun_datar} : {bangun.hitung_keliling()}")


if __name__ == "__main__" :
    hasil()