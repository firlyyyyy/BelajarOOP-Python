class Hero: # ==> template
    pass

hero1 = Hero() # ==> object / instance (instansiate)
hero2 = Hero()

hero1.name = "Alucard"
hero1.health = 200

hero2.name = "Grock"
hero2.health = 200

print(hero1.__dict__)
print(hero2.__dict__)
print("\n")
print(f"name hero: {hero1.name}, health: {hero1.health}")
print(f"name hero: {hero2.name}, health: {hero2.health}")