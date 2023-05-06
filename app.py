from flask import Flask, render_template, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_, static_folder='static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///signscribe.db"
db = SQLAlchemy(app)

class SignscribeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def repr(self):
        return '<User %r>' % self.name 

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/rest-project')
def rest_project():
    return send_file('notebooks/Rest Project.ipynb',
                     mimetype='application/json',
                     as_attachment=True,
                     attachment_filename='Rest Project.ipynb')

@app.route('/video-framing')
def video_framing():
    return send_file('notebooks/video_Framing.ipynb',
                     mimetype='application/json',
                     as_attachment=True,
                     attachment_filename='video_Framing.ipynb')

@app.route('/model')
def model():
    return send_file('notebooks/CNNModel.h5',
                     mimetype='application/json',
                     as_attachment=True,
                     attachment_filename='CNNModel.h5')

if _name_ == 'main':
    db.create_all()
    app.run(debug=True)