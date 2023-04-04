from flask import Flask, render_template, send_file

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
