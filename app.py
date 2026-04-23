from flask import Flask, render_template, request, redirect
import random
import profs
import func
import threading
import time

app = Flask(__name__)
app.debug = True
#global vars
moves = func.initMoves()
profemons = func.initProfs()
profemons = func.fixMoves(profemons, moves)
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
    return render_template('personal-stats.html')

@app.route('/team', methods=['GET','POST'])
def team():
    teamslot = 0
    msg = ""
    if request.method == 'POST':
        slot = request.form['slot']
        name = request.form['profname']
        
        #find profemon object from name
        nameindex = -1
        for i in profemons:
            nameindex += 1
            if i.name == name:
                break
        if slot == "-1": #remove a prof from team
            for i in player.team:
                if i.name == name:
                    teamslot = i.name.index(name)
            if teamslot == 0:
                player.team[0] = player.team[1]
                player.team[1] = player.team[2]
                player.team[2] = 0
            elif teamslot == 1:
                player.team[1] = player.team[2]
                player.team[2] = 0
            else:
                player.team[2] = 0
        elif slot == "0": #add to slot 1
            if profemons[nameindex] not in player.team:
                player.team[0] = profemons[nameindex]
            else:
                msg = "You can only have 1 of each Profemon on your team!"
        elif slot == "1": #add to slot 2
            if profemons[nameindex] not in player.team:
                player.team[1] = profemons[nameindex]
            else:
                msg = "You can only have 1 of each Profemon on your team!"
        else: #add to slot 3
            if profemons[nameindex] not in player.team:
                player.team[2] = profemons[nameindex]
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
    profemons = func.catchProf(profemons, "Delozier")
    tempProf = request.args.get('prof')
    workingProf = ""
    for i in profemons:
        if i.name == tempProf:
            workingProf = i
    return render_template('caretaking.html', data=workingProf)

@app.route('/forfeit/<profId>',methods=['GET'])
def forfeit_route(profId):
    print(f"Professor ID: {profId}")

@app.route('/battle', methods=['GET', 'POST'])
def battle():
    if request.method == 'POST' and 'move' in request.form:
        playerMove = request.form['move']
        if playerMove == "move1":
            move = player.currentProf.move1
        elif playerMove == "move2":
            move = player.currentProf.move2
        else:
            move = player.currentProf.move3
        bot_move = func.botMove(trainer, player)
        func.doMoves(move, bot_move, player, trainer) #Do status move logic
    return render_template('battle.html', player=player, trainer=trainer)

@app.route('/swap', methods=['POST'])
def swap():
    name = request.form['prof_name']
    for prof in player.team:
        if prof.name == name and not prof.fainted():
            if(not player.currentProf.fainted()):
                player.currentProf = prof
                move = "swap"
                bot_move = func.botMove(trainer, player)
                func.doMoves(move, bot_move, player, trainer)
                break
            else:
                player.currentProf = prof
                break
    return render_template('battle.html', player=player, trainer=trainer)

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