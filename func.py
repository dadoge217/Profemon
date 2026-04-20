from random import randint
from profs import Profemon, Move, player

types = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"]
profs = []
dmoves = ["Slap","Flamethrower","Bubble Burst","Thunderbolt","Razor Leaf","Icicle","Mega Punch","Sludge","Earth Shot","Skydive","Confusion","Slither","Rock Throw","Haunt","Dragon Claw","Bite","Iron Head","Moon Beam", "FINAL FLASH"]
smoves = ["Tangent","Insult","Good Boy","Gameover","Record","Bore","Ignore","Draw","Compliment"]

typeChart = [[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1],
             [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1],
             [1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1,1],
             [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1],
             [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1],
             [1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1],
             [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5],
             [1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,1],
             [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1],
             [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1],
             [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1],
             [1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5],
             [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1],
             [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0],
             [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,1,0.5],
             [1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2],
             [1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1]]

def initProfs():
    return profs

def critical():
    rand = randint(1, 26)
    if rand == 12:
        return True
    return False

def typeToNum(type):
    match type.lower():
        case "normal":
            return 0
        case "fire":
            return 1
        case "water":
            return 2
        case "electric":
            return 3
        case "grass":
            return 4
        case "ice":
            return 5
        case "fighting":
            return 6
        case "poison":
            return 7
        case "ground":
            return 8
        case "flying":
            return 9
        case "psychic":
            return 10
        case "bug":
            return 11
        case "rock":
            return 12
        case "ghost":
            return 13
        case "dragon":
            return 14
        case "dark":
            return 15
        case "steel":
            return 16
        case "fairy":
            return 17

def isEffective(aType, dType):
    t1 = typeToNum(aType)
    t2 = typeToNum(dType)
    mult = typeChart[t1][t2]
    return mult

def damageCalc(prof1, move, prof2):
    damage = (((((2 * 25) / 5) + 2) * move.power * (prof1.attack / prof2.defense)) / 50) + 2

    #check STAB
    if move.type == prof1.type:
        damage = damage * 1.5

    #do super effective
    damage = damage * isEffective(move.type, prof2.type)
    
    #random multiplier
    damage = damage * (randint(85, 100) / 100)

    #check critical
    if critical():
        damage = damage * 1.5
    
    return damage

def campaignBattle(trainer):
    playerProf1PO = False
    playerProf2PO = False
    playerProf3PO = False
    trainerProf1PO = False
    trainerProf2PO = False
    trainerProf3PO = False
    winner = ""

    currentTurn = 0
    battleEnded = False
    while(not battleEnded):
        currentTurn += 1
        botMove(trainer)
        #Do player turn
        if(player.currentProf.move == "swap"):
            continue
        if(trainer.currentProf.move == "swap"):
            continue
        if(player.currentProf.speed > trainer.currentProf.speed):
            if player.currentProf.move != "swap":
                damageCalc(player.currentProf, player.currentProf.move, trainer.currentProf)
            if trainer.currentProf.move != "swap":
                damageCalc(player.currentProf, trainer.currentProf.move, trainer.currentProf)
        if(trainer.currentProf.speed > player.currentProf.speed):
            if(trainer.currentProf.move != "swap"):
                damageCalc(trainer.currentProf, trainer.currentProf.move, player.currentProf)
            if player.currentProf.move != "swap":
                damageCalc(player.currentProf, player.currentProf.move, trainer.currentProf)
        if(playerProf1PO and playerProf2PO and playerProf3PO):
            battleEnded = True
            winner = "Trainer"
        elif(trainerProf1PO and trainerProf2PO and trainerProf3PO):
            battleEnded = True
            winner = "Player"



# class Move:
#     def __init__(self, type, power, status = ""):
#         self.type = type
#         self.power = power
#         self.status = status
def botMove(trainer):
    lowestDamage = 1
    if(isEffective(player.currentProf.type, trainer.currentProf.type) > 1):
        if(isEffective(player.currentProf.type, trainer.prof1.type) <= lowestDamage):
            profSwitch = trainer.prof1
            lowestDamage = isEffective(player.currentProf.type, trainer.prof1.type)
        if(isEffective(player.currentProf.type, trainer.prof2.type) <= lowestDamage):
            profSwitch = trainer.prof2
            lowestDamage = isEffective(player.currentProf.type, trainer.prof2.type)
        if(isEffective(player.currentProf.type, trainer.prof3.type) <= lowestDamage):
            profSwitch = trainer.prof3
        trainer.currentProf = profSwitch
        return "swap"
    if(isEffective(trainer.currentProf.move1, player.currentProf.type) > 1):
        return trainer.currentProf.move1
    elif(isEffective(trainer.currentProf.move2, player.currentProf.type) > 1):
        return trainer.currentProf.move2