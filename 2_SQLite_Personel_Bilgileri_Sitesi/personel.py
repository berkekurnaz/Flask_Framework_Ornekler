from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Berke/Desktop/PersonelBilgi/personel.db'
db = SQLAlchemy(app)


# Veritabani Sinifimiz
class Personel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adsoyad = db.Column(db.String(80))
    telefon = db.Column(db.String(40))
    yas = db.Column(db.Integer)
    maas = db.Column(db.Integer)
    bolum = db.Column(db.String(70))


# Ana Sayfa Gösterme Ve Personel Listeleme
@app.route("/")
def index():
    personeller = Personel.query.all()
    return render_template("index.html",personeller = personeller)

# Yeni Personel Ekleme Sayfasi
@app.route("/createPage")
def createPage():
    return render_template("createPage.html")    

# Yeni Personel Ekleme Islemi
@app.route("/create",methods=["POST"])
def create():
    adsoyad = request.form.get("adsoyad")
    telefon = request.form.get("telefon")
    yas = request.form.get("yas")
    maas = request.form.get("maas")
    bolum = request.form.get("bolum")
    newPersonel = Personel(adsoyad = adsoyad,telefon = telefon,yas = yas,maas = maas,bolum = bolum)
    db.session.add(newPersonel)
    db.session.commit()
    return redirect(url_for("index"))

# Personel Detay Sayfasi
@app.route("/readPage/<string:id>")
def readPage(id):
    personel = Personel.query.filter_by(id = id).first_or_404()
    return render_template("readPage.html",personel = personel)

# Personel Silme Islemi
@app.route("/delete/<string:id>")
def delete(id):
    personel = Personel.query.filter_by(id = id).first() 
    db.session.delete(personel)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
