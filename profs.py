class Profemon:
    def __init__(self, name, move1, move2, move3, stats, level=0, img=""):
        self.name = name
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.stats = stats
        self.level = level
        self.img = img

class Move:
    def __init__(self, type, power, status = ""):
        self.type = type
        self.power = power
        self.status = status