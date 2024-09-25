class Hero:
    def __init__(self, name):
        self.__health_full = [0, 100, 200, 300, 400, 500]
        self.__power_full = [0, 10, 20, 30, 40, 50]
        self.__armor_full = [0, 1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__level = 0
        self.__health = self.__health_full[self.__level]
        self.__power = self.__power_full[self.__level]
        self.__armor = self.__armor_full[self.__level]
        
    def info(self):
        print(f"{self.__name} \t| level {self.__level} \t| health {self.__health} \t| power {self.__power} \t| armor {self.__armor}")
        
        
    @property
    def health_full(self):
        return self.__health_full
    
    @property
    def power_full(self):
        return self.__power_full
    
    @property
    def armor_full(self):
        return self.__armor_full
    
    @property
    def levelUp(self):
        pass
    
    @property
    def gainExp(self):
        pass
    
    @health_full.setter
    def health_full(self, input):
        self.__health_full = input
        
    @power_full.setter
    def power_full(self, input):
        self.__power_full = input
        
    @armor_full.setter
    def armor_full(self, input):
        self.__armor_full = input
        
    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if (self.__exp >= 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100
            
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_full[self.__level]
        self.__power = self.__power_full[self.__level]
        self.__armor = self.__armor_full[self.__level]
        
            
class HeroIntel(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_full = [0, 50, 100, 150, 200, 250]
        self.power_full = [0, 20, 40, 60, 80, 100]
        self.armor_full = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        self.levelUp = 1
        
class HeroStrg(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_full = [0, 100, 200, 300, 400, 500]
        self.power_full = [0, 50, 100, 150, 200, 250]
        self.armor_full = [0, 2, 4, 6, 8, 10]
        self.levelUp = 1