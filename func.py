from random import randint
from profs import Profemon, Move, player

types = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"]
dmoves = ["Slap","Flamethrower","Bubble Burst","Thunderbolt","Razor Leaf","Icicle","Mega Punch","Sludge","Earth Shot","Skydive","Confusion","Slither","Rock Throw","Haunt","Dragon Claw","Bite","Iron Head","Moon Beam", "FINAL FLASH"]
smoves = ["Tangent","Insult","Good Boy","Gameover","Record","Bore","Ignore","Draw","Compliment"]
profstuff = [['Greg', 'POISON', 'Sludge', 'Earth Shot', 'Tangent', '61', '72', '57', '65', 'assets/images/base/greg.jpg'],
                ['Delozier', 'POISON', 'Sludge', 'Earth Shot', 'Tangent', '81', '102', '77', '85', 'assets/images/evos/delozier.png'],
                 
                ['Mikhail', 'FIRE', 'Flamethrower', 'Rock Throw', 'Insult', '58', '74', '58', '70', 'assets/images/base/mikhail.jpg'],
                ['Nesterenko', 'FIRE', 'Flamethrower', 'Rock Throw', 'Insult', '78', '104', '85', '94', 'assets/images/evos/nesterenko.png'],
                 
                ['Giovanni', 'GRASS', 'Razor Leaf', 'Bite', 'Good Boy', '60', '80', '80', '60', 'assets/images/base/giovanni.jpg'],
                ['Herrera', 'GRASS', 'Razor Leaf', 'Bite', 'Good Boy', '80', '100', '100', '80', 'assets/images/evos/harrera.png'],
                 
                ['John', 'WATER', 'Bubble Burst', 'Earth Shot', 'Insult', '59', '63', '80', '58', 'assets/images/base/jonathan.jpg'],
                ['Maletik', 'WATER', 'Bubble Burst', 'Earth Shot', 'Insult', '79', '83', '100', '78', 'assets/images/evos/maletic.png'],
                 
                ['Meldin', 'ELECTRIC', 'Thunderbolt', 'Razor Leaf', 'Gameover', '70', '80', '60', '45', 'assets/images/base/meldin.jpg'],
                ['Bektic', 'ELECTRIC', 'Thunderbolt', 'Razor Leaf', 'Gameover', '90', '115', '90', '55', 'assets/images/evos/bektic.png'],
                 
                ['Maha', 'PSYCHIC', 'Confusion', 'Flamethrower', 'Gameover', '64', '85', '60', '65', 'assets/images/base/maha.jpg'],
                ['Allouzi', 'PSYCHIC', 'Confusion', 'Flamethrower', 'Gameover', '80', '105', '90', '70', 'assets/images/evos/allouzi.png'],

                ['Deanna', 'NORMAL', 'Slap', 'Confusion', 'Record', '65', '70', '60', '65', 'assets/images/base/deanna.png'],
                ['Burret-Peffer', 'NORMAL', 'Slap', 'Confusion', 'Record', '75', '90', '61', '100', 'assets/images/evos/burritt-peffer.png'],
                 
                ['Javed', 'GROUND', 'Earth Shot', 'Mega Punch', 'Bore', '59', '66', '70', '35', 'assets/images/base/javed.jpg'],
                ['Khan', 'GROUND', 'Earth Shot', 'Mega Punch', 'Bore', '99', '86', '110', '40', 'assets/images/evos/khan.png'],
                 
                ['Qiang', 'GHOST', 'Haunt', 'Icicle', 'Ignore', '60', '60', '85', '85', 'assets/images/base/qiang.jpg'],
                ['Guan', 'GHOST', 'Haunt', 'Icicle', 'Ignore', '60', '60', '105', '105', 'assets/images/evos/guan.png'],
                 
                ['Hassan', 'FLYING', 'Skydive', 'Bubble Burst', 'Bore', '63', '60', '50', '71', 'assets/images/base/hassan.png'],
                ['Peyravi', 'FLYING', 'Skydive', 'Bubble Burst', 'Bore', '83', '80', '75', '101', 'assets/images/evos/peyravi.png'],
                 
                ['Rowan', 'DRAGON', 'Dragon Claw', 'Flamethrower', 'Insult', '61', '84', '70', '70', 'assets/images/base/rowan.jpg'],
                ['Ess', 'DRAGON', 'Dragon Claw', 'Flamethrower', 'Insult', '91', '100', '100', '80', 'assets/images/evos/ess.png'],
                 
                ['Raiful', 'ICE', 'Icicle', 'Bubble Burst', 'Gameover', '90', '60', '75', '45', 'assets/images/base/raiful.jpg'],
                ['Hasan', 'ICE', 'Icicle', 'Bubble Burst', 'Gameover', '110', '90', '90', '65', 'assets/images/evos/hasan.png'],
                 
                ['Joe', 'FIGHTING', 'Mega Punch', 'Thunderbolt', 'Gameover', '80', '85', '70', '45', 'assets/images/base/joe.jpg'],
                ['Demore', 'FIGHTING', 'Mega Punch', 'Thunderbolt', 'Gameover', '90', '105', '85', '55', 'assets/images/evos/demore.png'],
                 
                ['Charlie', 'BUG', 'Slither', 'Earth Shot', 'Draw', '35', '50', '35', '35', 'assets/images/base/charlie.jpg'],
                ['Burrows', 'BUG', 'Slither', 'Earth Shot', 'Draw', '65', '90', '80', '75', 'assets/images/evos/burrows.png'],
                 
                ['Gus', 'ROCK', 'Rock Throw', 'Earth Shot', 'Tangent', '55', '95', '45', '35', 'assets/images/base/augustine.jpg'],
                ['Samba', 'ROCK', 'Rock Throw', 'Earth Shot', 'Tangent', '80', '110', '65', '45', 'assets/images/evos/samba.png'],
                 
                ['Colin', 'STEEL', 'Iron Head', 'Rock Throw', 'Compliment', '60', '75', '80', '50', 'assets/images/base/colin.jpg'],
                ['Grant', 'STEEL', 'Iron Head', 'Rock Throw', 'Compliment', '80', '110', '90', '55', 'assets/images/evos/grant.png'],
                 
                ['Ben', 'FAIRY', 'Moon Beam', 'Iron Head', 'Gameover', '60', '50', '70', '60', 'assets/images/base/ben.jpg'],
                ['Purdum', 'FAIRY', 'Moon Beam', 'Iron Head', 'Gameover', '75', '71', '115', '80', 'assets/images/evos/purdum.png'],
                 
                ['Archie', 'DARK', 'Bite', 'Sludge', 'Draw', '63', '54', '41', '71', 'assets/images/base/archie.jpg'],
                ['Horne', 'DARK', 'Bite', 'Sludge', 'Draw', '103', '87', '61', '84', 'assets/images/evos/horne.png'],
                
                ['MEGA GRANT', 'STEEL', 'Iron Head', 'FINAL FLASH', 'Compliment', '80', '125', '120', '65', 'assets/images/evos/mega_grant.png']]

movestuff = [['Slap', 'NORMAL', '50', 'NULL'], #0
            ['Flamethrower', 'FIRE', '65', 'NULL'], #1
            ['Bubble Burst', 'WATER', '60', 'NULL'], #2
            ['Thunderbolt', 'ELECTRIC', '70', 'NULL'], #3
            ['Razor Leaf', 'GRASS', '65', 'NULL'], #4
            ['Icicle', 'ICE', '70', 'NULL'], #5
            ['Mega Punch', 'FIGHTING', '60', 'NULL'], #6
            ['Sludge', 'POISON', '65', 'NULL'], #7
            ['Earth Shot', 'GROUND', '60', 'NULL'], #8
            ['Skydive', 'FLYING', '65', 'NULL'], #9
            ['Confusion', 'PSYCHIC', '55', 'NULL'], #10
            ['Slither', 'BUG', '65', 'NULL'], #11
            ['Rock Throw', 'ROCK', '60', 'NULL'], #12
            ['Haunt', 'GHOST', '70', 'NULL'], #13
            ['Dragon Claw', 'DRAGON', '65', 'NULL'], #14
            ['Bite', 'DARK', '60', 'NULL'], #15
            ['Iron Head', 'STEEL', '70', 'NULL'], #16
            ['Moon Beam', 'FAIRY', '65', 'NULL'], #17
            ['FINAL FLASH', 'PSYCHIC', '80', 'NULL'], #18

            ['Tangent', 'NORMAL', '0', 'speed'], #19
            ['Insult', 'NORMAL', '0', 'defense'], #20
            ['Good Boy', 'NORMAL', '0', 'defense'], #21
            ['Gameover', 'NORMAL', '0', 'attack'], #22
            ['Record', 'NORMAL', '0', 'attack'], #23
            ['Bore', 'NORMAL', '0', 'speed'], #24
            ['Ignore', 'NORMAL', '0', 'attack'], #25
            ['Draw', 'NORMAL', '0', 'speed'], #26
            ['Compliment', 'NORMAL', '0', 'defense']] #27


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

def initMoves():
    moves = []
    for move in movestuff:
        moves.append(Move(move[0],move[1],move[2],move[3]))
    return moves

def initProfs():
    profemons = []
    for prof in profstuff:
        profemons.append(Profemon(prof[0],prof[1],prof[2],prof[3],prof[4],prof[5],prof[6],prof[7],prof[8],prof[9]))
    return profemons

def fixMoves(profemons, moves):
    for prof in profemons:
        #fix move1
        for m in moves:
            if prof.move1 == m.name:
                prof.move1 = m
                break
        #fix move2
        for m in moves:
            if prof.move2 == m.name:
                prof.move2 = m
                break
        #fix move3
        for m in moves:
            if prof.move3 == m.name:
                prof.move3 = m
                break
    return profemons

def catchProf(profemons, name):
    for i in profemons:
        if i.name == name:
            i.caught = True
            print(i.name)
            break
    return profemons

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