 
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

@app.route("/aluno")
def aluno():
    return jsonify({"nome": "Ruylis", "curso": "DSM", "disciplina": "Integração e Entrega Contínua"})

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/livros")
def livros():
    return jsonify({"livros": ["Python Fluente", "Clean Code", "O Programador Pragmático"]})

@app.route("/autores")
def autores():
    return jsonify({"autores": ["Luciano Ramalho", "Robert C. Martin", "Andrew Hunt"]})

if __name__ == "__main__":
    app.run(debug=True)
    