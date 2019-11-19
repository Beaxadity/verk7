from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key="vef"

mysql = MySQL(app)

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2210022020', password='borkur66', database='2210022020_verk7')
# https://pythonspot.com/login-authentication-with-flask/

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'pass' in request.form:
        username = request.form['user']
        password = request.form['pass']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE user = %s AND pass = %s', (user, pass))
    users = cursor.fetchone()
    if account:
            session['loggedin'] = True
            session['user'] = account['user']
            session['nafn'] = account['nafn']
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect username or password!'
    return render_template('index.html', msg='') 
    
@app.route('/signout')
def signout():
    session.pop('loggedin', None)
    session.pop('user', None)
    session.pop('nafn', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'pass' in request.form:
        username = request.form['user']
        password = request.form['pass']
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg)

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['user'])
    return redirect(url_for('login'))