## ==> constructor menggunakan __init__

class Hero: # ==> template
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
hero1 = Hero("udin", 200, 20)
hero2 = Hero("dudi", 200, 30)
print(hero1.__dict__)
print(hero2.__dict__)