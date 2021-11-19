from flask import Flask, request, render_template
from flask_mail import Mail, Message
   
app = Flask(__name__)
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'brainboyrichmond@gmail.com'
app.config['MAIL_PASSWORD'] = 'jkrexxewdtvfafoy'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
   
mail = Mail(app)

   
@app.route("/", methods=['GET', 'POST'])
def home():
    # try and except method
    #to avoid the app crashing if the message does not go through due to network or something
    try:
        if request.method == 'POST':
            sender = request.form['sender']
            recipient = request.form['recipient']
            message = request.form['message']
            subject = request.form['title']
            msg = Message(subject,sender=sender,recipients =[recipient] )
            msg.body = message
            mail.send(msg)
            return "message Sent"
        return render_template('mail.html')
    except Exception as e:
        return f'<p>{e} </p>'
    
   


if __name__ == '__main__':
   app.run(debug = True)