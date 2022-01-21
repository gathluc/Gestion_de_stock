import mysql.connector


def liste_fournisseur():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM fournisseur"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    return rows


def creer_fournisseur(nom, adresse, telephone, email):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO fournisseur (Nom_Four, Adress_Four, Tel_Four, Email) VALUES (%s, %s,%s, %s)"
    val = (nom, adresse, telephone, email)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
