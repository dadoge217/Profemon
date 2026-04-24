from flask import Flask, render_template, request, redirect
import random
import profs
import func
import threading
import time
import copy

app = Flask(__name__)
app.debug = True
#global vars
moves = func.initMoves()
profemons = func.initProfs()
profemons = func.fixMoves(profemons, moves)
perfectProfs = copy.deepcopy(profemons)
player = profs.Trainer()
profemons = func.catchProf(profemons, "Mikhail")
profemons = func.catchProf(profemons, "John")
profemons = func.catchProf(profemons, "Giovanni")
player = profs.Trainer("Ben", profemons[2], profemons[4], profemons[6])
trainer = profs.Trainer("bot1", profemons[1], profemons[5], profemons[7])
lock = threading.Lock()
wildProf = profemons[10]
showProf = False
counter = 0
timerVal = 10
running = False
catchOutcome = ""
inBattle = False
logs = []
personalStats = profs.PersonalStats()
trainers = [profs.Trainer("Bot 1", copy.deepcopy(profemons[0]), copy.deepcopy(profemons[4]), copy.deepcopy(profemons[6]), True),
            profs.Trainer("Bot 2", copy.deepcopy(profemons[8]), copy.deepcopy(profemons[14]), copy.deepcopy(profemons[18])),
            profs.Trainer("Bot 3", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[1])),
            profs.Trainer("Bot 4", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 5", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 6", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 7", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 8", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 9", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("Bot 10", copy.deepcopy(profemons[1]), copy.deepcopy(profemons[5]), copy.deepcopy(profemons[7])),
            profs.Trainer("FINAL BOT", copy.deepcopy(profemons[33]), copy.deepcopy(profemons[36]), copy.deepcopy(profemons[36]))]


def countdown():
    global timerVal, running, showProf, counter, profemons, catchOutcome
    running = True
    while timerVal > 0:
        time.sleep(1)
        timerVal -= 1
    roll = random.randint(1, 100)
    if counter >= roll:
        profemons = func.catchProf(profemons, wildProf.name)
        catchOutcome = f"Congrats! You caught a {wildProf.name}"
    else:
        catchOutcome = f"The {wildProf.name} got away!"
    running = False
    showProf = False #turn this into the part for logic, then counter = 0
    counter = 0
    timerVal = 10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('main-info.html', data=profemons)

@app.route('/prof', methods=['GET'])
def profPage():
    global profemons
    tempProf = request.args.get('prof')
    workingProf = ""
    for i in profemons:
        if i.name == tempProf:
            workingProf = i
    return render_template('dex-entry.html', data=workingProf)

@app.route('/stats')
def stats():
    global profemons
    count = 0
    for prof in profemons:
        if prof.caught == True:
            count+=1
    return render_template('personal-stats.html', personalStats=personalStats, count=count)

@app.route('/team', methods=['GET','POST'])
def team():
    teamslot = 0
    msg = ""
    if request.method == 'POST':
        slot = request.form['slot']
        getname = request.form['profname']
        print(getname)

        if slot == "-1":
            slot = -1
        elif slot == "0":
            slot = 0
        elif slot == "1":
            slot = 1
        else:
            slot = 2
        
        #find profemon object from name
        nameindex = -1
        teamslot = -1
        for i in profemons:
            nameindex += 1
            if i.name == getname:
                break
        if (slot == -1) and (profemons[nameindex].hp == profemons[nameindex].maxHP): #remove a prof from team
            for i in player.team:
                teamslot += 1
                if i != 0:
                    print("pass1")
                    print(i.name)
                    if i.name == getname:
                        print("pass2")
                        break
            player.team[teamslot] = 0
        else: #add to slot
            if (player.team[slot] == 0 or (profemons[nameindex] not in player.team and (player.team[slot].hp == player.team[slot].maxHP))):
                player.team[slot] = profemons[nameindex]
            elif ((profemons[nameindex].hp != profemons[nameindex].maxHP) or (player.team[slot].hp != player.team[slot].maxHP)):
                msg = "You cannot remove an injured Profemon from your team!"
            else:
                msg = "You can only have 1 of each Profemon on your team!"
    player.currentProf = player.team[0]
    return render_template('team-builder.html', team=player.team, totalProfs=profemons, msg=msg)

@app.route('/catch', methods=['GET', 'POST'])
def catch():
    global showProf, profemons, wildProf
    if request.method == 'POST' and 'look' in request.form:
        encounterChance = random.randint(1, 100)
        if encounterChance <= 97:
            wildProfNum = random.randint(0, 36)
            while (profemons[wildProfNum].caught):
                wildProfNum = random.randint(0, 36)
            wildProf = profemons[wildProfNum]
            showProf = True

    return render_template('catch.html', encounter=wildProf, show=showProf, catchOutcome=catchOutcome)

@app.route('/minigame', methods=['POST'])
def minigame():
    global showProf, counter, timerVal, running, catchOutcome

    if 'flee' in request.form:
        showProf = False
        return '', 204
    
    if 'click' in request.form:
        counter += 1
        with lock:
            if not running:
                running = True  # 🔥 set immediately inside lock
                timerVal = 10
                counter = 0
                catchOutcome = ""
                threading.Thread(target=countdown, daemon=True).start()

    return '', 204

@app.route('/timer')
def timer():
    return {
        "time": timerVal,
        "counter": counter,
        "show": showProf,
        "result": catchOutcome
    }

@app.route('/caretaking')
def caretaking():
    global profemons
    tempProf = request.args.get('prof')
    workingProf = ""
    for i in profemons:
        if i.name == tempProf:
            workingProf = i
    return render_template('caretaking.html', team=player.team)

@app.route('/pet', methods=['GET', 'POST'])
def care():
    if request.method == 'POST':
        idx = int(request.form.get('prof_index'))

        if player.team[idx] != 0:
            func.fullyheal(player.team[idx])

    return render_template('caretaking.html', team=player.team)

@app.route('/forfeit',methods=['GET', 'POST'])
def forfeit():
    global inBattle, trainer, logs, player
    logs = []
    inBattle = False
    msg = 'You lost! Heal your team and try again!'
    player.currentProf = player.team[0]
    for prof in trainer.team:
        func.fullyheal(prof)
    return render_template('battle.html', player=player, trainer=trainer, trainers=trainers, inBattle=inBattle, msg=msg)


@app.route('/battle', methods=['GET', 'POST'])
def battle():
    global player, trainer, trainers, inBattle, logs, personalStats, profemons
    teamgood = True
    msg = ''
    for prof in player.team:
        if prof == 0:
            teamgood = False
    if request.method == 'POST' and 'trainerID' in request.form:
        trainer_id = int(request.form['trainerID'])
        trainer = trainers[trainer_id]
        inBattle = True
        log = player.name + " vs " + trainer.name
        personalStats.appendBattle(log)

    elif request.method == 'POST' and 'move' in request.form:
        playerMove = request.form['move']
        if playerMove == "move1":
            move = player.currentProf.move1
        elif playerMove == "move2":
            move = player.currentProf.move2
        else:
            move = player.currentProf.move3
        bot_move = func.botMove(trainer, player, logs)
        func.doMoves(move, bot_move, player, trainer, logs, personalStats) #Do status move logic
        print("botmove")
        if((player.team[0].fainted() == True) and (player.team[1].fainted() == True) and (player.team[2].fainted() == True)):
            personalStats.losses += 1
            return redirect('/forfeit')
        elif((trainer.team[0].fainted() == True) and (trainer.team[1].fainted() == True) and (trainer.team[2].fainted() == True)):
            print("win")
            personalStats.wins += 1
            match trainer.name:
                case "Bot 1":
                    trainers[1].shown = True
                case "Bot 2":
                    trainers[2].shown = True
                case "Bot 3":
                    trainers[3].shown = True
                case "Bot 4":
                    trainers[4].shown = True
                case "Bot 5":
                    trainers[5].shown = True
                case "Bot 6":
                    trainers[6].shown = True
                case "Bot 7":
                    trainers[7].shown = True
                case "Bot 8":
                    trainers[8].shown = True
                case "Bot 9":
                    trainers[9].shown = True
                case "Bot 10":
                    trainers[10].shown = True
            randInt = random.randint(0,2)
            selected_prof = player.team[randInt]
            name = selected_prof.name
            full_index = -1
            for i, prof in enumerate(profemons):
                if prof.name == name:
                    full_index = i
                    break
            if full_index != -1 and full_index < len(profemons) - 1:
                next_prof = profemons[full_index + 1]
                profemons = func.catchProf(profemons, next_prof.name)
            inBattle = False
            msg = "You won!"
            
    elif not teamgood:
        msg = "You must have 3 team members to battle!"
        return render_template('team-builder.html', team=player.team, totalProfs=profemons, msg=msg)
    return render_template('battle.html', player=player, trainer=trainer, trainers=trainers, inBattle=inBattle, logs=logs, msg=msg)

@app.route('/swap', methods=['POST'])
def swap():
    global player, trainer, trainers, inBattle, logs, personalStats
    name = request.form['prof_name']
    for prof in player.team:
        if prof.name == name and not prof.fainted():
            if(not player.currentProf.fainted()):
                player.currentProf = prof
                move = "swap"
                temp = player.name + " switched to " + player.currentProf.name
                logs.append(temp)
                bot_move = func.botMove(trainer, player, logs)
                func.doMoves(move, bot_move, player, trainer, logs, personalStats)
                break
            else:
                player.currentProf = prof #To do: Resets (forfeiting and changing page should reset trainer profemon), stats page, working on in-game consoles, pretty up the main page, get status moves to work, get feed button to do something, make hp bar dynamic?
                temp = player.name + " switched to " + player.currentProf.name
                logs.append(temp)
                break   
    return render_template('battle.html', player=player, trainer=trainer, trainers=trainers, inBattle=inBattle, logs=logs)

@app.route('/unlockall')
def unlock():
    global profemons
    for i in profemons:
        i.caught = True
    return redirect('/')

@app.route('/relockall')
def relock():
    global profemons
    for i in profemons:
        i.caught = False
    profemons = func.catchProf(profemons, "Mikhail")
    profemons = func.catchProf(profemons, "John")
    profemons = func.catchProf(profemons, "Giovanni")
    return redirect('/')

if __name__ == "__main__":
    profemons = func.catchProf(profemons, "Mikhail")
    profemons = func.catchProf(profemons, "John")
    profemons = func.catchProf(profemons, "Giovanni")
    player = profs.Trainer("Ben", profemons[2], profemons[4], profemons[6])
    app.run()