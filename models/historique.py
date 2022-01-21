import mysql.connector


def achats():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM achat"
    mycursor.execute(sql)
    achats = mycursor.fetchall()
    return achats


def approvisionnements():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM approvi"
    mycursor.execute(sql)
    approvisionnements = mycursor.fetchall()
    return approvisionnements
