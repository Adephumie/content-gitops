from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Demonstrating my hands-on tutorial on ACG for GitOps"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
