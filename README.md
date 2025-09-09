# 📝 Todo List & Server Health App

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

A modern **Flask Web Application** with an interactive **Todo List** and a **Server Health** dashboard.

---

## ⚡ Features

- ✅ Add / Update / Delete tasks  
- ✅ Mark tasks as **Pending / Completed**  
- ✅ Automatic **date & time** on tasks  
- ✅ Delete confirmation pop-up  
- ✅ Modern animated loader ✨  
- ✅ Server health: CPU %, Memory %, Disk, Uptime  

---

## 🚀 Run Locally

```bash
git clone https://github.com/roni3132/todo_app.git
cd todo_app
pip install -r requirements.txt
python app.py
```
👉 Open in your browser: http://127.0.0.1:5000

## 🐳 Run with Docker 


```bash
git clone https://github.com/roni3132/todo_app.git
cd todo_app/
docker build -t todoapp:latest .
docker run -d -p 5000:5000 todoapp:latest

```

👉 Open in your browser:

Local: http://localhost:5000

AWS EC2: http://<your-ec2-public-ip>:5000


---


