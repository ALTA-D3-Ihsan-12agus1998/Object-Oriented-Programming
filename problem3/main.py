# tulis solusi code disini

class Kalkulator :
    def __init__(self, pertama, kedua) :
        self.pertama = pertama
        self.kedua = kedua

    def penjumlahan(self) :
        hasil = self.pertama + self.kedua
        return hasil

    def pengurangan(self) :
        hasil = self.pertama - self.kedua
        return hasil

    def perkalian(self) :
        hasil = self.pertama * self.kedua
        return hasil

    def pembagian(self) :
        hasil = self.pertama / self.kedua
        return hasil

def main() :
    pertama = float(input("Masukkan angka pertama: "))
    kedua = float(input("Masukkan angka kedua: "))

    operasi = input("Pilih operasi (+, -, *, /) : ")

    if operasi == "+" :
        hasil = Kalkulator(pertama, kedua).penjumlahan()
        operasi_str = "Penjumlahan"
    elif operasi == "-" :
        hasil = Kalkulator(pertama, kedua).pengurangan()
        operasi_str = "Pengurangan"
    elif operasi == "*" :
        hasil = Kalkulator(pertama, kedua).perkalian()
        operasi_str = "Perkalian"
    elif operasi == "/" :
        hasil = Kalkulator(pertama, kedua).pembagian()
        operasi_str = "Pembagian"
    else :
        print("Operasi tidak valid")
        return

    print(f"{operasi_str} : {hasil}")


if __name__ == "__main__" :
    main()