class Hero:
    
    def __init__(self, name, health, demage, armor):
        self.name = name
        self.health = health
        self.demage = demage
        self.armor = armor
        
    def serang(self, musuh):
        print(f"{self.name} menyerang {musuh.name}")
        musuh.diserang(self, self.demage)
        
    def diserang(self, musuh, demageLawan):
        print(f"{self.name} diserang {musuh.name}")
        attackMusuh = demageLawan / self.armor
        print(f"demage musuh: {str(attackMusuh)}")
        self.health -= attackMusuh
        print(f"darah {self.name} tersisia {str(self.health)}")
        
heroPertama = Hero("naruto", 200, 50, 20)
heroKedua = Hero("pain", 200, 30, 50)

heroPertama.serang(heroKedua)
print("\n")
heroKedua.serang(heroPertama)
