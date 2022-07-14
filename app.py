from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sparten.loyola@gmail.com'
app.config['MAIL_PASSWORD'] = os.envirson.get('Gmail')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/")
def projects():
    return render_template("projectTab.html")

@app.route("/about/", methods=["POST, ", "GET"])
def about():
    if request.method == "POST":
        flash("Email has been sent!", "info")
        return render_template("index.html")
    else:
        return render_template("aboutTab.html")
    
    # Check for Captcha when submit button is pressed

if __name__ == "__main__":
    app.run(debug=True)