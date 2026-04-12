import sqlite3

database = sqlite3.connect("myAwesomeActualDatabase.db")
dbCurser = database.cursor()
dbCurser.execute("CREATE TABLE profemonInfo(name, move1, move2, move3, hp, attack, defense, speed, img)")
dbCurser.execute("""
    INSERT INTO profemonInfo VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
