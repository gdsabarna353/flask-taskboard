from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/health")
def get_health():
    return jsonify({"status": "ok"}), 200

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
        return jsonify(tasks), 200

@app.route("/tasks/<int:id>", methods=['PUT', 'DELETE'])
def updateAndDelete_tasks(id):
    # global tasks
    # task_found = False
    if(request.method == 'PUT'):
        for task in tasks:
            if(task['id'] == id):
                # task_found = True
                task['completed'] = True
                return jsonify(task), 200
    elif(request.method == 'DELETE'):
        for task in tasks:
            if(task['id'] == id):
                # newtasks = filter(lambda task: task['id'] != int(id), tasks)
                # tasks = list(newtasks)
                tasks.remove(task)
                # tasks.pop(int(id)-1)
                return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)