from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def hello_world():
    return "<p>Hello, World guys!</p>"

@app.route("/health", methods=['GET'])
def get_health():
    if(request.method == 'GET'):
        return {
            "status": "ok"
        }

@app.route('/tasks', methods=['GET', 'POST'])
def post_tasks():
    if(request.method == 'POST'):
        data = request.get_json()
        print(data)
        new_task = {
            "id": len(tasks)+1,
            "title": data['title'],
            "description": data['description'],
            "completed": False
        }
        tasks.append(new_task)
        return jsonify(new_task), 201
    else:
        return tasks, 200

app.run(debug=True)