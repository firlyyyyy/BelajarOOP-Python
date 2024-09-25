"""" ==>> GETTER AND SETTER <<== """

class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.__umur = umur
        # self.__info = "nama: {} \numur: {}".format(nama, umur)
    
    
    @property
    def info(self):
        # return self.__info
        return "nama: {} \numur: {}".format(self.nama, self.__umur)
    
    # ==> GETTER <==
    # def get_nama(self):
    #     return self.__nama
    
    # def get_umur(self):
    #     return self.__umur
    
    @property
    def umur(self):
        pass
    
    # ==> getter
    @umur.getter
    def umur(self):
        return self.__umur
    
    # ==> setter
    @umur.setter
    def umur(self, inputUmur):
        self.__umur = inputUmur
        
    # ==> deleter
    @umur.deleter
    def umur(self):
        print("umur di hapus")
        self.__umur = None

orangPertama = Orang("Dudi", 27)

print("merubah info")    
print(orangPertama.info)

print("\n")

print("merubah getter dan setter")
print(orangPertama.umur) # ==> sebelum di ubah
print(orangPertama.__dict__)

orangPertama.umur = 20
print(orangPertama.umur) # ==> setelah di ubah
print(orangPertama.__dict__)

del orangPertama.umur
print(orangPertama.__dict__)

# orangPertama.nama = "Ucup"
# print(orangPertama.info)
# print(f"nama: {orangPertama.get_nama()}\numur: {orangPertama.get_umur()}")