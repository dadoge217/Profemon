class Profemon:
    def __init__(self, name, move1, move2, move3, stats, hp, attack, defense, speed, img=""):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.stats = stats
        self.HP = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.img = img

class Move:
    def __init__(self, type, name, power, status = ""):
        self.type = type
        self.name = name
        self.power = power
        self.status = status

class Trainer:
    def __init__(self, name, prof1, prof2, prof3):
        self.name = name
        self.prof1 = prof1
        self.prof2 = prof2
        self.prof2 = prof3