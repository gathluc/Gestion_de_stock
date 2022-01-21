import mysql
from flask import *
import mysql.connector


def login():
    msg = ''
    if request.method == 'POST':
        adminName = request.form['adminName']
        adminPassword = request.form['adminPassword']
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM admin WHERE adminName= %s AND adminPassword=%s"
        val = (adminName, adminPassword)
        mycursor.execute(sql, val)
        record = mycursor.fetchone()
        if record:
            session['loggedin'] = True
            session['adminName'] = record[1]
            return redirect(url_for('home'))
        else:
            msg = 'Le nom et/ou le mot de passe incorrect!'
    return render_template('authenticate.html', msg=msg)
