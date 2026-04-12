import sqlite3

database = sqlite3.connect("myAwesomeActualDatabase.db")
dbCurser = database.cursor()
dbCurser.execute("CREATE TABLE profemonInfo(name TEXT PRIMARY KEY, move1 TEXT, move2 TEXT, move3 TEXT, hp INTEGER, attack INTEGER, defense INTEGER, speed INTEGER, img TEXT)")
dbCurser.execute("""
    INSERT INTO profemonInfo VALUES
                ('Greg', 'Sludge', 'Earth Shot', 'Tangent', '61', '72', '57', '65'),
                ('Delozier', 'Sludge', 'Earth Shot', 'Tangent', 81', '102', '77', '85'),
                 
                ('Mikhail', 'Flamethrower', 'Rock Slide', 'Insult', '58', '74', '58', '70'),
                ('Nesterenko', 'Flamethrower', 'Rock Slide', 'Insult', '78', '104', '85', '94'),
                 
                ('Giovanni', 'Razor Leaf', 'Bite', 'Good Boy', '60', '80', '80', '60'),
                ('Herrera', 'Razor Leaf', 'Bite', 'Good Boy', '80', '100', '100', '80'),
                 
                ('John', 'Bubble Burst', 'Earth Shot', 'Insult', '59', '63', '80', '58'),
                ('Maletik', 'Bubble Burst', 'Earth Shot', 'Insult', '79', '83', '100', '78'),
                 
                ('Meldin', 'Thunderbolt', 'Razor Leaf', 'Gameover', '70', '80', '60', '45'),
                ('Bektic', 'Thunderbolt', 'Razor Leaf', 'Gameover', '90', '115', '90', '55'),
                 
                ('Maha', 'Confusion', 'Flamethrower', 'Gameover', '64', '85', '60', '65'),
                ('Allouzi', 'Confusion', 'Flamethrower', 'Gameover', '80', '105', '90', '70'),
                 
                
""")
