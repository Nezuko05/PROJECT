from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/landingpage')
def landingpage():
    return render_template('landingpage.html')






if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)