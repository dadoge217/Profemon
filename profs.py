class Profemon:
    def __init__(self, name, type, move1, move2, move3, hp, attack, defense, speed, img):
        self.name = name
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.HP = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.img = img

class Move:
    def __init__(self, name, type, power, status = ""):
        self.type = type
        self.name = name
        self.power = power
        self.status = status

class Trainer:
    def __init__(self, prof1 = "none", prof2 = "none", prof3 = "none", name = "player"):
        self.name = name
        self.prof1 = prof1
        self.prof2 = prof2
        self.prof2 = prof3
        self.currentProf = prof1

player = Trainer()