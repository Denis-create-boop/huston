
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run()





