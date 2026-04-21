from flask import Flask, render_template, request, redirect
import profs
import func

app = Flask(__name__)
app.debug = True
moves = func.initMoves()
profemons = func.initProfs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('main-info.html', data=profemons)

@app.route('/prof', methods=['GET'])
def profPage():
    tempProf = request.args.get('prof')
    workingProf = ""
    for i in profemons:
        if i.name == tempProf:
            workingProf = i
    print(workingProf.name)
    return redirect('/info')

@app.route('/stats')
def stats():
    return render_template('personal-stats.html')

@app.route('/team')
def team():
    return render_template('team-builder.html')

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