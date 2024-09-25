class Hero:
    # ==> class variable
    jumlah_hero = 0

    def __init__(self, nameHero, levelHero, healthHero, demageHero):
        # ==> instance variable
        self.name = nameHero
        self.level = levelHero
        self.health = healthHero
        self.demage = demageHero
        Hero.jumlah_hero += 1

        # ==> void function | method function | tanpa return
    def heroPertama(self):
        print(f"""Name Hero: {self.name}
Level Hero: {self.level}
Heatlh Hero: {self.health}
Demage Hero: {self.demage}""")

    def heroKedua(self):
        print(f"""Name Hero: {self.name}
Level Hero: {self.level}
Heatlh Hero: {self.health}
Demage Hero: {self.demage}""")

        # ==> void function | method function | menggunakan argumen
    def upHero(self, upLevel, upHealth, upDemage):
        self.level += upLevel
        self.health += upHealth
        self.demage += upDemage
        
        # ==> void function | method function | menggunakan return
    def get(self):
        return self.name, self.health, self.demage, self.level
        
    # def jumlahHero(Hero):
    #     return f"jumlah hero = {Hero.jumlah_hero}"

hero1 = Hero("Miya", 15, 200, 20)
hero2 = Hero("Gusion", 13, 180, 50)

print(f"{30*'=':^30}")
print(f"{'sebelum di upgrade':^30}")
print(f"{30*'=':^30}")

hero1.heroPertama()
print(f"{30*'-':^30}")
hero2.heroKedua()

print("\n")

print(f"{30*'=':^30}")
print(f"{'sebelum di upgrade':^30}")
print(f"{30*'=':^30}")

hero1.upHero(5, 50, 30)
hero1.heroPertama()
print(f"{30*'-':^30}")
hero2.upHero(2, 20, 20)
hero2.heroKedua()

print("\n")

print(hero1.get())

# print(Hero.jumlah_hero)

""" ==> STATIC METHOD dan CLASS METHOD <== """
class Orang:
    __jumlahOrang = 0
    def __init__(self, name):
        self.__name = name
        Orang.__jumlahOrang += 1
        
    # ==> method ini hanya berlaku untuk objek, jika selain objek tidak bisa
    def getJumlah(self):
        return Orang.__jumlahOrang
    
    # ==> method ini tidak berlaku untuk objek, tapi berlaku untuk class
    def getJumlah1():
        return Orang.__jumlahOrang
    
    # ==> menggunakan static method (decorator) bakal nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Orang.__jumlahOrang
    
    # ==> menggunakan class method (decorator) bakal nempel ke class aja
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlahOrang
        
orangPertama = Orang("Udin")
orangKedua = Orang("Ucup")
orangKetiga = Orang("Cipung")
print(f"jumlah orang: {Orang.getJumlah3()}")
