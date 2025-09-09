from flask import Flask, render_template, request, redirect, url_for
import psutil, datetime

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route("/")
def index():
    uptime_seconds = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    health = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": str(uptime_seconds).split('.')[0]
    }

    pending = [t for t in todos if not t["completed"]]
    completed = [t for t in todos if t["completed"]]

    return render_template("index.html", todos=todos, pending=pending, completed=completed, health=health)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    todos.append({"task": task, "completed": False, "time": timestamp})
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete(task_id):
    todos[task_id]["completed"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    todos.pop(task_id)
    return redirect(url_for("index"))

@app.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    new_task = request.form.get("task")
    if new_task:
        todos[task_id]["task"] = new_task
        todos[task_id]["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

