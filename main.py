from flask import *
from models.client import *
from models.marchandises import *
from models.fournisseur import *
from models.historique import *
from mysql.connector import cursor
from models.admin import *

app = Flask(__name__)
app.secret_key = "super secret key"

connection = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="",
                                     database="gestion_stock")

cursor = connection.cursor()


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('adminName', None)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        adminName = request.form['adminName']
        adminPassword = request.form['adminPassword']
        cursor.execute('SELECT * FROM admin WHERE adminName= %s AND adminPassword=%s', (adminName, adminPassword), )
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['adminName'] = record[1]
            return redirect(url_for('home'))
        else:
            msg = 'Name/password incorrect!'
    return render_template('authenticate.html',
                           msg=msg)


@app.route('/')
def authenticate():
    return render_template('authenticate.html')


@app.route('/home')
def home():
    row = liste_marchandise()
    fournisseur = liste_fournisseur()
    client = liste_clients()
    return render_template('home.html', adminName=session['adminName'], row=row, fournisseur=fournisseur, client=client)


@app.route('/liste_client')
def liste_client():
    row = liste_clients()
    return render_template('liste_clients.html', row=row)


@app.route('/create_client', methods=['POST'])
def create_client():
    nom = request.form['nom']
    adresse = request.form['adresse']
    telephone = request.form['numéro']
    email = request.form['email']
    insert_client(nom, adresse, telephone, email)
    return redirect("/liste_client")


@app.route('/liste_fournisseur')
def liste_four():
    row = liste_fournisseur()
    return render_template('liste_fournisseur.html', row=row)


@app.route('/create_fournisseur', methods=['POST'])
def create_fournisseur():
    nom = request.form['nom']
    adresse = request.form['adresse']
    telephone = request.form['numéro']
    email = request.form['email']
    creer_fournisseur(nom, adresse, telephone, email)
    return redirect("/liste_fournisseur")


@app.route('/create', methods=['POST'])
def create_item():
    Ref_Four = request.form['Ref_Four']
    Date_fourni = request.form['Date_fourni']
    Ref_Mar = request.form['Ref_Mar']
    Marchandises = request.form['Marchandises']
    Quantité = request.form['Quantité']
    inserer_marchandise(Ref_Mar, Marchandises, Quantité)
    insert_his_Fourni(Date_fourni, Quantité, Ref_Four, Ref_Mar)
    return redirect('/home')


@app.route('/retrieve', methods=['POST'])
def retrieve():
    Ref_Client = request.form['Ref_Client']
    Date_Achat = request.form['Date_Achat']
    Quantité = 0 - int(request.form['Quantité'])
    Ref_Mar = request.form['Ref_Mar']
    insert_his_achat(Date_Achat, Quantité, Ref_Client, Ref_Mar)
    update_quantite(Quantité, Ref_Mar)
    return redirect('/home')


@app.route('/supply', methods=['POST'])
def supply():
    Ref_Four = request.form['Ref_Four']
    Date_fourni = request.form['Date_fourni']
    Quantité = request.form['Quantité']
    Ref_Mar = request.form['Ref_Mar']
    insert_his_Fourni(Date_fourni, Quantité, Ref_Four, Ref_Mar)
    update_quantite(Quantité, Ref_Mar)
    return redirect('/home')


@app.route('/Historique')
def historique():
    approvi = approvisionnements()
    achat = achats()
    return render_template('historique.html', approvi=approvi, achat=achat)


if __name__ == "__main__":
    app.run(debug=True)
