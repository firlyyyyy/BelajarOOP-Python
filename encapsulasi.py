class Buku:
    def __init__(self, judul, pengarang) -> None:
        self.__judul = judul
        self.__pengarang = pengarang
        
        
    # ==> getter
    def getJudul(self):
        return self.__judul
    
    def getPengarang(self):
        return self.__pengarang
    
    # ==> setter
    def setJudul(self):
        self.__judul = "Ucup sang Penyelamat"
        return self.__judul # ==> harus menggunakan return agar dapat mengambil datanya
        
        
buku = Buku("Perjalanan Superhero", "ucup")
print(buku.__dict__)
print(f"""Judul Buku: {buku.setJudul()}
Pengarang Buku: {buku.getPengarang()}""")
