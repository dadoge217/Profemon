class Profemon:
    def __init__(self, name, type, move1, move2, move3, hp, attack, defense, speed, img):
        self.name = name
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.hp = int(hp)
        self.maxHP = int(hp)
        self.attack = int(attack)
        self.maxAttack = int(attack)
        self.defense = int(defense)
        self.maxDefense = int(defense)
        self.speed = int(speed)
        self.maxSpeed = int(speed)
        self.img = img
        self.caught = False
    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    def fainted(self):
        if self.hp == 0: 
            return True
        return False

class Move:
    def __init__(self, name, type, power, status = ""):
        self.type = type
        self.name = name
        self.power = int(power)
        self.status = status

class Trainer:
    def __init__(self, name = "player", prof1 = "none", prof2 = "none", prof3 = "none",):
        self.name = name
        self.team = []
        self.team.append(prof1)
        self.team.append(prof2)
        self.team.append(prof3)
        self.currentProf = prof1

player = Trainer()