import os

class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun_terbit
        
    def informsi_buku(self):
        return print(f"Judul Buku: {self.judul}\nPengarang: {self.pengarang}\nTahun Terbit: {self.tahun}".title())

while True:
    os.system("clear")
    
    # ==> Header
    print(f"{30*'-':^30}")
    print(f"{'masukkan buku':^30}".upper())
    print(f"{30*'-':^30}")
    print("\n")
    
    buku = Buku(input("judul buku: ".title()), input("pengarang buku: ".title()), input("tahun terbit: ".title()))
    
    print(f"\n{30*'-':^30}")
    print(f"{'data buku':^30}".upper())
    print(f"{30*'-':^30}\n")
    
    buku.informsi_buku()
    
    isDone = input("\napakan selesai? (n / y) ")
    if isDone == "y":
        break