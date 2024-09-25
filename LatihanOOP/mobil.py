class Mobil:
    
    def __init__(self, merk_mobil, model_mobil, tahun_mobil):
        self.merk = merk_mobil
        self.model = model_mobil
        self.tahun = tahun_mobil
        
    def informasi_mobil(self):
        return f"mobil {self.merk} {self.model}, tahun {self.tahun}".title()
    
inputMobil = Mobil(input("merk mobil : "), input("model mobil : "), input("tahun mobil : "))

print(inputMobil.informasi_mobil())
