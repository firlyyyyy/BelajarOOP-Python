class Orang:
    
    def __init__(self, nama, umur) -> None:
        self.nama = nama
        self.umur = umur
        
        # ==> variable instance private
        self.__private = "private"
        
        # ==> variable instance protected
        self._protected = "protected"
        
namaPertama = Orang("Budi", 20)
print(namaPertama.__dict__)
namaPertama._protected = "testing"
print(namaPertama.__dict__)