""" ==>> SUPER INHERITANCE <<== """

class Orang:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        
    def info(self):
        print(f"{self.nama} memiliki gaji {self.gaji}")
        
class OrangPenting(Orang):
    def __init__(self, nama):
        # Orang.__init__(self, nama, "10.000.000")
        super().__init__(nama, "10.000.000")
        super().info()
        
class OrangBiasa(Orang):
    def __init__(self, nama):
        # Orang.__init__(self, nama, "1.000.000")
        super().__init__(nama, "1.000.000")
        super().info()
        
ucup =  OrangPenting('ucup')
udir = OrangBiasa('udir')
