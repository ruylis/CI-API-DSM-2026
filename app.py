 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API CI/CD funcionando!"})

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/sobre")
def sobre():
    return jsonify({"projeto": "CI-API-DSM-2026", "aluno": "Ruylis", "semestre": "1º DSM"})

if __name__ == "__main__":
    app.run(debug=True)