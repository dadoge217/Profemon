from flask import Flask, render_template, request, redirect
import random
import profs
import func

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
wildProf = profemons[1]
showProf = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('main-info.html', data=profemons)

@app.route('/prof', methods=['GET'])
def profPage():
    global profemons
    profemons = func.catchProf(profemons, "Delozier")
    tempProf = request.args.get('prof')
    workingProf = ""
    for i in profemons:
        if i.name == tempProf:
            workingProf = i
    return render_template('dex-entry.html', data=workingProf)

@app.route('/stats')
def stats():
    return render_template('personal-stats.html')

@app.route('/team')
def team():
    return render_template('team-builder.html', team=player.team, totalProfs=profemons)

@app.route('/catch', methods=['GET', 'POST'])
def catch():
    global showProf
    if request.method == 'POST' and 'look' in request.form:
        encounterChance = random.randint(1, 100)
        if encounterChance <= 97:
            showProf = True

    return render_template('catch.html', encounter=wildProf, show=showProf)

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
        func.doMoves(move, bot_move, player, trainer)
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

if __name__ == "__main__":
    profemons = func.catchProf(profemons, "Mikhail")
    profemons = func.catchProf(profemons, "John")
    profemons = func.catchProf(profemons, "Giovanni")
    player = profs.Trainer("Ben", profemons[2], profemons[4], profemons[6])
    app.run()