from flask import Flask,render_template,request
import requests

app = Flask(__name__)

url = "https://api.github.com/users/"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        kullaniciAdi = request.form.get("kullaniciAdi")

        response_kullanici = requests.get(url + kullaniciAdi)
        response_depolar = requests.get(url + kullaniciAdi + "/repos")
        response_takipciler = requests.get(url + kullaniciAdi + "/followers")
        response_takipler = requests.get(url + kullaniciAdi + "/following")

        kullanici_bilgileri = response_kullanici.json()
        depo_bilgileri = response_depolar.json()
        takipci_bilgileri = response_takipciler.json()
        takip_bilgileri = response_takipler.json()

        if "message" in kullanici_bilgileri:
            return render_template("index.html",hataMesaj = "Böyle Bir Kullanici Bulunamadi...")
        else:
            return render_template("index.html",kullanici = kullanici_bilgileri,depo = depo_bilgileri,takipciler = takipci_bilgileri,takipler = takip_bilgileri)    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)    