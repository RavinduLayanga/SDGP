from app import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

from app import send_file

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

@app.route('/sign-language-model')
def sign_language_model():
    return send_file('notebooks/Copy of Model for sign language recognition for 1GB dataset.ipynb',
                     mimetype='application/json',
                     as_attachment=True,
                     attachment_filename='Model for sign language recognition.ipynb')

