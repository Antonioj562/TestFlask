from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sparten.loyola@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('mailP')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/")
def projects():
    return render_template("projectTab.html")

@app.route("/about/", methods=["POST", "GET"])
def about():
    if request.method == "POST":
        senderSub = request.form.get("subject")
        senderEmail = request.form.get("email")
        senderMes = request.form.get("message")

        msg = Message("Portfolio Message: "+str(senderSub), 
                        sender="no-reply@domain.com", 
                        recipients=['antoniojloyola@gmail.com'])
        msg.body = "Email: " + str(senderEmail) +' --- '+senderMes
        mail.send(msg)
        return render_template("index.html")
    return render_template("aboutTab.html")
    
    # Check for Captcha when submit button is pressed

if __name__ == "__main__":
    app.run()