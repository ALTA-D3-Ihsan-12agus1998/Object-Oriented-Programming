# tulis solusi code disini

class BangunDatar:
    def __init__(self, nama) :
        self.nama = nama

class Kubus(BangunDatar) :
    def __init__(self, nama, sisi) :
        super().__init__(nama)
        self.sisi = sisi

    def hitung_volume(self) :
        return self.sisi ** 3

class Balok(BangunDatar) :
    def __init__(self, nama, panjang, lebar, tinggi) :
        super().__init__(nama)
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self) :
        return self.panjang * self.lebar * self.tinggi

class Tabung(BangunDatar) :
    def __init__(self, nama, jarijari, tinggi) :
        super().__init__(nama)
        self.jarijari = jarijari
        self.tinggi = tinggi

    def hitung_volume(self) :
        return 3.1415 * self.jarijari ** 2 * self.tinggi

def Hasil() :
    sisi_kubus = float(input("Masukkan sisi kubus: "))

    panjang_balok = float(input("Masukkan panjang balok: "))
    lebar_balok = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))

    jarijari_tabung = float(input("Masukkan jari-jari tabung: "))
    tinggi_tabung = float(input("Masukkan tinggi tabung: "))

    kubus = Kubus("Kubus", sisi_kubus)
    balok = Balok("Balok", panjang_balok, lebar_balok, tinggi_balok)
    tabung = Tabung("Tabung", jarijari_tabung, tinggi_tabung)

    print(f"\nHasil perhitungan volume:")
    print(f"Volume {kubus.nama}: {kubus.hitung_volume():.2f}")
    print(f"Volume {balok.nama}: {balok.hitung_volume():.2f}")
    print(f"Volume {tabung.nama}: {tabung.hitung_volume():.2f}")


if __name__ == "__main__" :
    Hasil()