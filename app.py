from flask import Flask,render_template,request
from flask_ngrok import run_with_ngrok

app   = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()