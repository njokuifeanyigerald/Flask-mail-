from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)
mail = Mail(app) #discover the Mail library
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
   

   
@app.route("/")
def home():
    # try and except method
    #to avoid the app crashing if the message does not go through duw to network or something
    try:
        msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['individual@gmail.com'])
        msg.body = "Hello Africa"
        mail.send(msg)
        return "Sent"
    except Exception as e:
        return f'<p>{e} </p>'
    
   


if __name__ == '__main__':
   app.run(debug = True)