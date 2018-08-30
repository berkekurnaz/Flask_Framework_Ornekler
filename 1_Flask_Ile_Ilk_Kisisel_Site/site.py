from flask import Flask,render_template,flash,redirect,url_for,session,logging,request

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")    

@app.route("/education")
def education():
    return render_template("education.html")    

@app.route("/skills")
def skills():
    return render_template("skills.html")    

@app.route("/awards")
def awards():
    return render_template("awards.html")    

@app.route("/contact")
def contact():
    return render_template("contact.html")
    


if __name__ == "__main__":
    app.run(debug=True)
