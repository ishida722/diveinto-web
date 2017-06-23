from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from diveinto.db_controller import DBcon

app = Flask(__name__)

def GetDbCon():
    dbCon = DBcon()
    with open('.diveinto', 'r') as f:
        dbCon.MakeTree(f)
    return dbCon

def Commit(dbCon):
    with open('.diveinto', 'w') as f:
        dbCon.Commit(f)

@app.route('/')
def show_entries():
    dbCon = DBcon()
    with open('.diveinto', 'r') as f:
        dbCon.MakeTree(f)
    tasks = dbCon.ChildTaskNames()
    return render_template('top.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def AddNewTask():
    dbCon = GetDbCon()
    dbCon.AddTask(request.form['name'])
    Commit(dbCon)
    return redirect(url_for('show_entries'))

