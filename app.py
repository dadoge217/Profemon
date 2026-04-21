from flask import Flask, render_template, request, redirect
import profs
import func

app = Flask(__name__)
app.debug = True
#global vars
moves = func.initMoves()
profemons = func.initProfs()
profemons = func.fixMoves(profemons, moves)
player = profs.Trainer()

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

@app.route('/battle')
def battle():
    return render_template('battle.html')

@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/caretaking')
def caretaking():
    return render_template('caretaking.html')

@app.route('/forfeit/<profId>',methods=['GET'])
def forfeit_route(profId):
    print(f"Professor ID: {profId}")

if __name__ == "__main__":
    profemons = func.catchProf(profemons, "Mikhail")
    profemons = func.catchProf(profemons, "John")
    profemons = func.catchProf(profemons, "Giovanni")
    player = profs.Trainer("Ben", profemons[2], profemons[4], profemons[6])
    app.run()