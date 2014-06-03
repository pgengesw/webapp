# executemany() method


import sqlite3

with sqlite3.connect("webapp.db") as connection:
	c = connection.cursor()
	
	#insert multiple records using a tuple
	players = [
			('Humza', 'Akbar', 'Pistons', 26),
			('Tharsan', 'Genges','Spurs', 24),
			('John', 'Doe','Heatles', 22),
			('Sanjay', 'Path', 'Thunder', 22),
			('Russel', 'Fernandes', 'Cavs', 26),
			('Sean', 'Elliot', 'Spurs', 27),
			('Reggie', 'Miller', 'Pacers', 25),
			('Tay', 'Prince', 'Pistons', 24),
			('Al', 'Horford', 'Hawks', 24),
			('Dwayne', 'Wade', 'Heatles', 25),
			('Timmy', 'Duncan', 'Spurs', 26)
			]
	
	#insert data into table
	c.executemany('INSERT INTO users VALUES (?,?,?,?)', players)