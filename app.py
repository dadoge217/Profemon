from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('main-info.html')

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