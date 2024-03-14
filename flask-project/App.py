from flask import Flask, render_template, send_file


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/show_API', methods=['POST'])
def show_api():
    return 'Something'


app.run(debug=True)
