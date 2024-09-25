class PersegiPanjang:

    def __init__(self, panjang, lebar) -> None:
        self.panjang = panjang
        self.lebar = lebar

    def menghitung_luas(self):
        if self.panjang <= 0 or self.lebar <= 0:
            return "Panjang dan lebar tidak boleh 0 atau kurang"
        return f"luas persegi panjang = {self.panjang * self.lebar}"

    def menghitung_keliling(self):
        if self.panjang <= 0 or self.lebar <= 0:
            return "Panjang dan lebar tidak boleh 0 atau kurang"
        return f"keliling persegi panjang = {2 * (self.panjang + self.lebar)}"


angka = PersegiPanjang(int(float(input("masukkan panjang = "))), int(float(input("masukkan lebar = "))))
print(angka.menghitung_luas())
print(angka.menghitung_keliling())
