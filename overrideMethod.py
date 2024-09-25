""" ==>> OVERRIDE METHOD <<== """


class Orang:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def info(self):
        print(f"{self.nama} dengan jabatan {self.jabatan}")


class Orang_penting(Orang):
    def __init__(self, nama):
        super().__init__(nama, "boss")

    # ==>> override
    def info(self):
        print(f"{self.nama} dengan jabatan {self.jabatan} | gaji : 10.000.000")


class Orang_biasa(Orang):
    def __init__(self, nama):
        super().__init__(nama, "karyawan")

    # ==>> override
    def info(self):
        print(f"{self.nama} dengan jabatan {self.jabatan} | gaji : 1.000.000")


deden = Orang_penting('deden')
pew = Orang_biasa('pew')

deden.info()
pew.info()
