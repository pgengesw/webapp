from flask import *
import sqlite3
import os

DATABASE = 'webapp.db'
app = Flask(__name__)
app.config.from_object(__name__)

#error handling
app.config["DEBUG"] = True
 
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/welcome')
def welcome():
	g.db = connect_db()
	cur = g.db.execute('select firstname, lastname, team, age from users')
	users = [dict(firstname=row[0], lastname=row[1], team=row[2], age=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('welcome.html', users=users)
	

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)