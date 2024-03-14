from flask import (Flask, render_template,
                   jsonify)


app = Flask(__name__)


api_example = {
    "Name": "Lucas",
    "Git": "/lucasgommes",
    "Language": "Python, Java",
    "Framwork": "Flask, Spring"
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/show_API', methods=['POST'])
def show_api():
    return jsonify(api_example)


app.run(debug=True)
