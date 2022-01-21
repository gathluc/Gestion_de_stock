import mysql.connector


def liste_marchandise():
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM stock"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    return rows


def inserer_marchandise(Ref_mar, Marchandises, Quantité):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO stock (Ref_Mar,Marchandise,Quantite) VALUES (%s,%s,%s)"
    val = (Ref_mar, Marchandises, Quantité)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()


def insert_his_Fourni(Date_Fourni, Quantité, Ref_Four, Ref_mar):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO approvi (Date_fourni,Quant_Fourni,Ref_Four,Ref_Mar) VALUES ('%s',%s,'%s','%s')" % (
        Date_Fourni, Quantité, Ref_Four, Ref_mar)
    mycursor.execute(sql)
    mydb.commit()


def insert_his_achat(Date_Achat, Quant_Achat, Ref_Client, Ref_Mar):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO achat (Date_Achat, Quant_Achat, Ref_Client, Ref_Mar) VALUES ('%s',%s,'%s','%s')" % (
        Date_Achat, Quant_Achat, Ref_Client, Ref_Mar)
    mycursor.execute(sql)
    mydb.commit()


def update_quantite(Quantité, Ref_Mar):
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_stock")
    mycursor = mydb.cursor()
    sql = "UPDATE stock SET Quantite = Quantite + %s WHERE Ref_Mar = '%s'" % (Quantité, Ref_Mar)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
