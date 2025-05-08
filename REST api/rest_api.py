from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a REST API", "done": False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify({"message": "Task added successfully!"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task.update(request.json)
            return jsonify({"message": "Task updated successfully!"})
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
