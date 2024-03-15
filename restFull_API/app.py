import json
from flask import (Flask, render_template,
                   jsonify, request)


app = Flask(__name__)


devs = [
    {"id": 0, "name": "Lucas", "languages": ["Python", "Java"]},
    {"id": 1, "name": "Maria", "languages": ["JavaScript", "C#"]},
    {"id": 2, "name": "João", "languages": ["Ruby", "PHP"]}
]


@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def dev(id):
        if request.method == "GET":
            try:
                resp = devs[id]
            except IndexError:
                    msg = 'Developer with ID {} not exist.'.format(id)
                    resp = {'Status': "error", "Message: ":msg}
            except Exception:
                msg = "Operation error."
                resp = {"status": "error", "message": msg}
            return jsonify(resp)
        
        elif request.method == "PUT":
            data = json.loads(request.data)
            devs[id] = data
            return jsonify(data)
        
        elif request.method == "DELETE":
            devs.pop(id)
            return jsonify({"Status": "Succes"})
        
@app.route('/dev', methods=["POST", "GET"])
def add_dev():
    if request.method == "POST":
         data = json.loads(request.data)
         new_dev = {
              "id": len(devs),
              "name": data["name"],
              "languages": data["languages"]
         }
         devs.append(new_dev)
         return jsonify(new_dev)
    elif request.method == "GET":
         return jsonify(devs)

app.run(debug=True)

devs.update()
