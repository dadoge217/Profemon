class Profemon:
    def __init__(self, name, move1, move2, move3, stats, HP, attack, defense, speed, level=0, img=""):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.stats = stats
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.img = img
        
class Move:
    def __init__(self, type, power, status = ""):
        self.type = type
        self.power = power
        self.status = status