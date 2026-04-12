class Profemon:
    def __init__(self, name, move1, move2, move3, type, HP, attack, defense, speed, img=""):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.type = type
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.img = img

class Move:
    def __init__(self, type, power, status = ""):
        self.type = type
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