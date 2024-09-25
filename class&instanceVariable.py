## ==> Class dan Instance variable

class Hero: # ==> template
    
    ## ==> class variable
    jumlah = 0
    
    def __init__(self, name, health, attack):
        ## ==> instance variable
        self.name = name
        self.health = health
        self.attack = attack
        Hero.jumlah += 1
        print(f"""Name hero: {name}
Health: {health}
Attack: {attack}""")
        
hero1 = Hero("udin", 200, 20)
print(Hero.jumlah)
hero2 = Hero("dudi", 200, 30)
print(Hero.jumlah)