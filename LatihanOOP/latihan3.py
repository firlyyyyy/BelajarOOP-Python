class Hero:

    # ==>> private class
    __jumlah = 0

    def __init__(self, name, health, power, armor):
        self.__name = name
        self.__healthStandar = health
        self.__powerStandar = power
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__power = self.__powerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__healt = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name} level {self.__level} : \thealth \t\t: {self.__healt}/{self.__healthMax} \n\t\tpower \t\t: {self.__power} \n\t\tarmor \t\t: {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'up level')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__power = self.__powerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            
    def attack(self, musuh):
        self.gainExp = 50


jet = Hero('jet', 100, 3, 5)
pripun = Hero('pripun', 100, 2, 3)

print(jet.info)

jet.attack(pripun)
jet.attack(pripun)
jet.attack(pripun)
jet.attack(pripun)
jet.attack(pripun)
jet.attack(pripun)

print(jet.info)


# print(jet.__dict__)
