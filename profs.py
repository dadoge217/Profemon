class Profemon:
    def __init__(self, name, type, move1, move2, move3, hp, attack, defense, speed, img):
        self.name = name
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.img = img
        self.caught = False
        def takeDamage(damage):
            hp = hp - damage

class Move:
    def __init__(self, name, type, power, status = ""):
        self.type = type
        self.name = name
        self.power = power
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