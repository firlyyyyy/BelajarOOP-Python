import os

class Mahasiswa:

    def __init__(self, nama, nim, jurusan, nilai1, nilai2, nilai3):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai1 = int(nilai1)
        self.nilai2 = int(nilai2)
        self.nilai3 = int(nilai3)
        # self.ipk = ipk

    def informasi_mahasiswa(self):
        return f"nama \t\t: {self.nama}\nNIM \t\t: {self.nim}\njurusan \t: {self.jurusan}"

    def informasi_nilai(self):
        return self.nilai1 + self.nilai2 + self.nilai3

    def hitung_ipk(self):
        rataRata = self.informasi_nilai() / 3

        if rataRata >= 80:
            return 4.0
        elif rataRata >= 75:
            return 3.5
        elif rataRata >= 70:
            return 3.0
        elif rataRata >= 65:
            return 2.5
        elif rataRata >= 60:
            return 2.0
        else:
            return 1.0


while True:
    os.system("clear")
    print(f"{30*'-':^30}")
    print(f"{'masukkan data':^30}".upper())
    print(f"{30*'-':^30}\n")

    data = Mahasiswa(
        input("masukkan nama \t\t: "),
        int(input("masukkan nim \t\t: ")),
        input("masukkan jurusan \t: "),
        int(input("nilai 1 \t\t: ")),
        int(input("nilai 2 \t\t: ")),
        int(input("nilai 3 \t\t: "))
    )

    print(f"\n{30*'-':^30}")
    print(f"{'data mahasiswa':^30}".upper())
    print(f"{30*'-':^30}\n")

    print(data.informasi_mahasiswa())
    print(f"total nilai \t: {data.informasi_nilai()}")
    print(f"IPK \t\t: {data.hitung_ipk()}")
    
    isDone = input("apakah udah selesai? (y / n) ")
    if isDone == "y":
        break

print("program selesai")