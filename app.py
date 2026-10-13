from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Jenkins CI/CD Lab - Version 1"

@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
