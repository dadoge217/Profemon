import sqlite3

database = sqlite3.connect("myAwesomeActualDatabase.db")
dbCurser = database.cursor()
dbCurser.execute("CREATE TABLE profemonInfo(name TEXT PRIMARY KEY, type TEXT, move1 TEXT, move2 TEXT, move3 TEXT, hp INTEGER, attack INTEGER, defense INTEGER, speed INTEGER, img TEXT)")
dbCurser.execute("""
    INSERT INTO profemonInfo VALUES
                ('Greg', 'POISON', 'Sludge', 'Earth Shot', 'Tangent', '61', '72', '57', '65'),
                ('Delozier', 'POISON', 'Sludge', 'Earth Shot', 'Tangent', 81', '102', '77', '85'),
                 
                ('Mikhail', 'FIRE', 'Flamethrower', 'Rock Slide', 'Insult', '58', '74', '58', '70'),
                ('Nesterenko', 'FIRE', 'Flamethrower', 'Rock Slide', 'Insult', '78', '104', '85', '94'),
                 
                ('Giovanni', 'GRASS', 'Razor Leaf', 'Bite', 'Good Boy', '60', '80', '80', '60'),
                ('Herrera', 'GRASS', 'Razor Leaf', 'Bite', 'Good Boy', '80', '100', '100', '80'),
                 
                ('John', 'WATER', 'Bubble Burst', 'Earth Shot', 'Insult', '59', '63', '80', '58'),
                ('Maletik', 'WATER', 'Bubble Burst', 'Earth Shot', 'Insult', '79', '83', '100', '78'),
                 
                ('Meldin', 'ELECTRIC', 'Thunderbolt', 'Razor Leaf', 'Gameover', '70', '80', '60', '45'),
                ('Bektic', 'ELECTRIC', 'Thunderbolt', 'Razor Leaf', 'Gameover', '90', '115', '90', '55'),
                 
                ('Maha', 'PSYCHIC', 'Confusion', 'Flamethrower', 'Gameover', '64', '85', '60', '65'),
                ('Allouzi', 'PSYCHIC', 'Confusion', 'Flamethrower', 'Gameover', '80', '105', '90', '70'),

                ('Deanna', 'NORMAL', 'Slap', 'Confusion', 'Record', '65', '70', '60', '65'),
                ('Burret-Peffer', 'NORMAL', 'Slap', 'Confusion', 'Record', '75', '90', '61', '100'),
                 
                ('Javed', 'GROUND', 'Earth Shot', 'Mega Punch', 'Bore', '59', '66', '70', '35'),
                ('Khan', 'GROUND', 'Earth Shot', 'Mega Punch', 'Bore', '99', '86', '110', '40'),
                 
                ('Qiang', 'GHOST', 'Haunt', 'Icicle', 'Ignore', '60', '60', '85', '85'),
                ('Guan', 'GHOST', 'Haunt', 'Icicle', 'Ignore', '60', '60', '105', '105'),
                 
                ('Hassan', 'FLYING', 'Skydive', 'Bubble Burst', 'Bore', '63', '60', '50', '71'),
                ('Peyravi', 'FLYING', 'Skydive', 'Bubble Burst', 'Bore', '83', '80', '75', '101'),
                 
                ('Rowan', 'DRAGON', 'Dragon Claw', 'Flamethrower', 'Insult', '61', '84', '70', '70'),
                ('Ess', 'DRAGON', 'Dragon Claw', 'Flamethrower', 'Insult', '91', '100', '100', '80'),
                 
                ('Raiful', 'ICE', 'Icicle', 'Bubble Burst', 'Gameover', '90', '60', '75', '45'),
                ('Hasan', 'ICE', 'Icicle', 'Bubble Burst', 'Gameover', '110', '90', '90', '65'),
                 
                ('Joe', 'FIGHTING', 'Mega Punch', 'Thunderbolt', 'Gameover', '80', '85', '70', '45'),
                ('Demore', 'FIGHTING', 'Mega Punch', 'Thunderbolt', 'Gameover', '90', '105', '85', '55'),
                 
                ('Charlie', 'BUG', 'Slither', 'Earth Shot', 'Draw', '35', '50', '35', '35'),
                ('Burrows', 'BUG', 'Slither', 'Earth Shot', 'Draw', '65', '90', '80', '75'),
                 
                ('Gus', 'ROCK', 'Rock Throw', 'Earth Shot', 'Tangent', '55', '95', '45', '35'),
                ('Samba', 'ROCK', 'Rock Throw', 'Earth Shot', 'Tangent', '80', '110', '65', '45'),
                 
                ('Colin', 'STEEL', 'Iron Head', 'Rock Throw', 'Compliment', '60', '75', '80', '50'),
                ('Grant', 'STEEL', 'Iron Head', 'Rock Throw', 'Compliment', '80', '110', '90', '55'),
                ('MEGA GRANT', 'STEEL', 'Iron Head', 'FINAL FLASH', 'Compliment', '80', '125', '120', '65'),
                 
                ('Ben', 'FAIRY', 'Moon Beam', 'Iron Head', 'Gameover', '60', '50', '70', '60'),
                ('Purdum', 'FAIRY', 'Moon Beam', 'Iron Head', 'Gameover', '75', '71', '115', '80'),
                 
                ('Archie', 'DARK', 'Bite', 'Sludge', 'Draw', '63', '54', '41', '71'),
                ('Horne', 'DARK', 'Bite', 'Sludge', 'Draw', '103', '87', '61', '84'),
""")

dbCurser.execute("CREATE TABLE moveInfo(name TEXT PRIMARY KEY, type TEXT, power INTEGER, status TEXT NULL)")
dbCurser.execute("""
    INSERT INTO moveInfo VALUES
                 ('Slap', 'NORMAL', '50', 'NULL'),
                 ('Flamethrower', 'FIRE', '65', 'NULL'),
                 ('Bubble Burst', 'WATER', '60', 'NULL'),
                 ('Thunderbolt', 'ELECTRIC', '70', 'NULL'),
                 ('Razor Leaf', 'GRASS', '65', 'NULL'),
                 ('Icicle', 'ICE', '70', 'NULL'),
                 ('Mega Punch', 'FIGHTING', '60', 'NULL'),
                 ('Sludge', 'POISON', '65', 'NULL'),
                 ('Earth Shot', 'GROUND', '60', 'NULL'),
                 ('Skydive', 'FLYING', '65', 'NULL'),
                 ('Confusion', 'PSYCHIC', '55', 'NULL'),
                 ('Slither', 'BUG', '65', 'NULL'),
                 ('Rock Throw', 'ROCK', '60', 'NULL'),
                 ('Haunt', 'GHOST', '70', 'NULL'),
                 ('Dragon Claw', 'DRAGON', '65', 'NULL'),
                 ('Bite', 'DARK', '60', 'NULL'),
                 ('Iron Head', 'STEEL', '70', 'NULL'),
                 ('Moon Beam', 'FAIRY', '65', 'NULL'),
                 ('FINAL FLASH', 'PSYCHIC', '80', 'NULL'),

                 ('Tangent', 'NORMAL', '0', 'speed'),
                 ('Insult', 'NORMAL', '0', 'defense'),
                 ('Good Boy', 'NORMAL', '0', 'defense'),
                 ('Gameover', 'NORMAL', '0', 'attack'),
                 ('Record', 'NORMAL', '0', 'attack'),
                 ('Bore', 'NORMAL', '0', 'speed'),
                 ('Ignore', 'NORMAL', '0', 'attack'),
                 ('Draw', 'NORMAL', '0', 'speed'),
                 ('Compliment', 'NORMAL', '0', 'defense'),
""")