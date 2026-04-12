from random import randint
from profs import Profemon, Move

types = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"]
profs = []
dmoves = ["Slap","Flamethrower","Bubble Burst","Thunderbolt","Razor Leaf","Icicle","Mega Punch","Sludge","Earth Shot","Skydive","Confusion","Slither","Rock Throw","Haunt","Dragon Claw","Bite","Iron Head","Moon Beam"]
smoves = ["Tangent","Insult","Good Boy","Gameover","Record","Bore","Ignore"]

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