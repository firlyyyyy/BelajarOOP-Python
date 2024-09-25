class Biodata:

    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = int(umur)
        self.alamat = alamat
        
    def get_nama(self) -> str:
        return self.nama
    
    def get_umur(self) -> str:
        return self.umur
    
    def get_alamat(self) -> str:
        return self.alamat
    
biodata = Biodata(input("masukkan nama: ",), input("masukkan umur: "), input("masukkan alamat: "))

print(f"nama anda {biodata.get_nama()}, anda berumur {biodata.get_umur()}, dan anda tinggal di {biodata.get_alamat()}")