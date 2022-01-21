import mysql.connector


def liste_clients():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM client"
    mycursor.execute(sql)
    clients = mycursor.fetchall()
    return clients


def insert_client(nom, adresse, telephone, email):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO client (Nom_Client, Address_Client, Tel_Client, Email_Client) VALUES (%s, %s,%s, %s)"
    val = (nom, adresse, telephone, email)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()


def update_clients(id, nom, adresse, telephone, email):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "UPDATE client SET Nom_Client = '%s' , Address_Client = '%s' , Tel_Client = '%s' , Email_Client = '%s' WHERE Ref_Client = %d"
    val = (nom, adresse, telephone, email, id)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
