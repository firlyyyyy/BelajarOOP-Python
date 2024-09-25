""" ==>> MAGIC METHOD <<== """

class Buah:
    
    def __init__(self, nama, jumlah) -> None:
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self) -> str:
        return f"buah {self.nama} ada {self.jumlah} biji"
            
    def __add__(self, objek):
        return f"jumlah buah pertama {self.jumlah} sama jumlah buah kedua {objek.jumlah} = {self.jumlah + objek.jumlah}"
        
buah1 = Buah('mangga', 10)
buah2 = Buah('durian', 20)
print(buah1 + buah2)