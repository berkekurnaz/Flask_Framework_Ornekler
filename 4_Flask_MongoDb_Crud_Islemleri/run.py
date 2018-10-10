from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RehberUygulama" 
mongo = PyMongo(app)



# Index Sayfası Ve Rehberdeki Kisileri Listeleme
@app.route("/")
def index():
    name = mongo.db.Rehber.find()
    count = mongo.db.Rehber.count()
    return render_template("index.html",name = name,count = count)



# Yeni Kisi Ekle Sayfası Get Islemi
@app.route("/createPage")
def createPage():
    return render_template("createPage.html") 

# Yeni Kisi Ekleme Islemi
@app.route("/create",methods=["POST"])
def create():
    name = request.form.get("name")
    email = request.form.get("email")
    phonenumber = request.form.get("phonenumber")
    person = mongo.db.Rehber.insert({"Name": name, "Email": email, "PhoneNumber": phonenumber})
    return redirect(url_for("index"))



# Kisi Oku Sayfasina Verilerin Gonderilmesi
@app.route("/readPage/<Name>")
def readPage(Name):
    person = mongo.db.Rehber.find_one_or_404({"_id": ObjectId(Name)})
    return render_template("readPage.html",person = person)



# Kisi Guncelle Sayfasi Veriyi Gonderme
@app.route("/updatePage/<Name>")
def updatePage(Name):
    person = mongo.db.Rehber.find_one_or_404({"_id": ObjectId(Name)})
    return render_template("updatePage.html",person = person)

# Kisi Guncelleme Islemi
@app.route("/update/<Name>",methods=["POST"])
def update(Name):
    name = request.form.get("name")
    email = request.form.get("email")
    phonenumber = request.form.get("phonenumber")
    myquery = { "_id" : ObjectId(Name) }
    newValues = { "$set": { "Name": name, "Email": email, "PhoneNumber": phonenumber}} 
    person = mongo.db.Rehber.update_one(myquery,newValues)
    return redirect(url_for("index"))



# Delete Sayfasi Ve Silinecek Kisi Bilgilerinin Gosterilmesi
@app.route("/deletePage/<Name>")
def deletePage(Name):
    person = mongo.db.Rehber.find_one_or_404({ "_id": ObjectId(Name)})
    return render_template("deletePage.html",person = person)    

# Kisi Silme Islemi
@app.route("/delete/<Name>") 
def delete(Name):
    person = mongo.db.Rehber.delete_one( {"_id": ObjectId(Name)})
    return redirect(url_for("index"))


    
if __name__ == "__main__":
    app.run(debug=True)