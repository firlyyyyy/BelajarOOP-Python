""" ==>> INHERITANCE (PEWARISAN) <<== """

class Orang:
    
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
        
class Orang_penting(Orang):
    pass

class Orang_berguna(Orang):
    pass

ucup = Orang('ucup', 17)
udin = Orang_penting('udin', 19)
udung = Orang_berguna('udung', 20)

print(f"dari class Orang \t\t| nama : {ucup.nama} \t| umur : {ucup.umur}")
print(f"dari class Orang_penting \t| nama : {udin.nama} \t| umur : {udin.umur}")
print(f"dari class Orang_berguna \t| nama : {udung.nama} \t| umur : {udung.umur}")