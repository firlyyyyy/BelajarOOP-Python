class Kalkulator:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def tambah(self) -> int:
        return self.a + self.b
    
    def kurang(self) -> int:
        return self.a - self.b
    
    def kali(self) -> int:
        return self.a * self.b
    
    def bagi(self) -> int:
        if self.b == 0:
            return "angka tidak boleh nol"
        else:
            return self.a / self.b
        
calc = Kalkulator(int(input("masukkan nilai a: ")), int(input("masukkan nilai b: ")))

print(f"hasil tambah = {calc.tambah()}")
print(f"hasil kurang = {calc.kurang()}")
print(f"hasil kali   = {calc.kali()}")
print(f"hasil bagi   = {calc.bagi()}")